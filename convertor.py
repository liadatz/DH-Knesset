import os
import subprocess


def opener(path, flags):
    return os.open(path, flags, 0o777)


def create_sh_file():
    f.write("echo Start Converting Files\n")
    doc_path = "./downloadedFiles/"
    file_list = os.scandir(doc_path)
    for file in file_list:
        file_name = file.name
        if file_name.split(".")[1] == "txt":
            continue
        f.write('soffice --headless --convert-to "txt:Text (encoded):UTF8" --outdir {} {}\n'
                .format(doc_path, doc_path + file_name))
        f.write('echo {} converting done\n'.format(file_name))
        f.write('rm {}\n'.format(doc_path + file_name))
    f.write('echo TASK IS DONE')


os.umask(0)  # Without this, the created file will have 0o777 - 0o022 (default umask) = 0o755 permissions
f = open("./convertor_to_txt.sh", "w", opener=opener)
f.write("#!/bin/bash\n\n")
create_sh_file()
f.close()
