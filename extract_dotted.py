import os


def get_lemma(file_name):
    f = open(file_name, "r", encoding='utf-8')
    output = ""
    for line in f:
        lemma = line.split(' ')
        if len(lemma) > 1:
            lemma = lemma[1]
            output = output + lemma + '\n'
    f.close()
    return output


path = "./downloadedFilesTaggedDotted/"
file_list = os.scandir(path)
for file in file_list:
    file_path = path + file.name
    s = get_lemma(file_path)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(s)
