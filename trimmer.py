import codecs
import re
import os


def trim_files():
    path = "./downloadedFiles/"
    file_list = os.scandir(path)
    for file in file_list:
        file_name = file.name
        file_path = path + file_name
        with open(file_path, 'rt', encoding="utf8") as myfile:  # Open txt for reading text
            contents = myfile.read()  # Read the entire file to a string
        x = re.search("דברי.?.?.?הסבר", contents)
        if x is not None:
            (_, start_index) = x.span()
        else:
            start_index = contents.find("דברי - הסבר", 0) + 11
            if start_index == 10:
                start_index = contents.find("דברי-הסבר", 0) + 9
            if start_index == 8:
                start_index = contents.find("דברי – הסבר", 0) + 11
            if start_index == 10:
                print(file_path, "failed to find start")
                f.write(file_path + " failed to find start\n")

        end_index = contents.find("הצעת חוק זהה", start_index)
        if end_index == -1:
            end_index = contents.find("--", start_index)
        if end_index == -1:
            print(file_path, "failed to find end")
            f.write(file_path + " failed to find end\n")
        with codecs.open(file_path, "w", "utf-8-sig") as newfile:
            newfile.write(contents[start_index:end_index])


f = open("log_error.txt", "a")
trim_files()
f.close()
