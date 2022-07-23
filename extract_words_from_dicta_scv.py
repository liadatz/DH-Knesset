import os
import csv


def extract_words(src_path, dst_path):
    f = open(dst_path, 'w', encoding='utf-8')
    with open(src_path, newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i = 0
        for row in spamreader:
            if i == 0:
                i += 1
                continue
            string = ', '.join(row)
            split = string.split("\t")
            if len(split) > 4:
                if len(split[2]) > 1:
                    f.write(split[2] + '\n')
    f.close()


knesset_numbers = ["K17"]
male_corpus_path = './{}/male_dicta_csv/'
female_corpus_path = './{}/female_dicta_csv/'
for knesset in knesset_numbers:
    # # male
    # male_csvs_path = male_corpus_path.format(knesset)
    # male_file_list = os.scandir(male_csvs_path)
    # for file in male_file_list:
    #     file_name = file.name
    #     short_file_name = file_name.split(".")[0]
    #     extract_words(male_csvs_path + file_name,
    #                   "./{}/male_corpus_extracted/{}".format(knesset, short_file_name + '.txt'))
    # female
    female_csvs_path = female_corpus_path.format(knesset)
    female_file_list = os.scandir(female_csvs_path)
    for file in female_file_list:
        file_name = file.name
        short_file_name = file_name.split(".")[0]
        extract_words(female_csvs_path + file_name,
                      "./{}/female_corpus_extracted/{}".format(knesset, short_file_name + '.txt'))
