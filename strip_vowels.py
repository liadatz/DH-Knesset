import os
import re


def strip_vowels(file_name):
    f = open(file_name, "r", encoding='utf-8')
    output = ""
    for line in f:
        new_line = re.sub(r'[\u0591-\u05C7]', '', line)
        output = output + new_line
    f.close()
    return output


path = "./downloadedFilesTaggedDotted/"
file_list = os.scandir(path)
for file in file_list:
    file_path = path + file.name
    s = strip_vowels(file_path)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(s)
