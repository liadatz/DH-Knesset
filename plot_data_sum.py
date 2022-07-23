import matplotlib.pyplot as plt
import numpy as np

import csv


def create_plot(m_percentages, f_percentages, labels, merge_topics, redundant_topics):
    topic_to_remove = []
    for (a, b) in merge_topics:
        m_percentages[a] += m_percentages[b]
        f_percentages[a] += f_percentages[b]
        topic_to_remove.append(b)
    for topic in redundant_topics:
        topic_to_remove.append(topic)
    topic_to_remove.sort(reverse=True)
    for topic in topic_to_remove:
        m_percentages.pop(topic)
        f_percentages.pop(topic)
    left = []
    for value in range(len(m_percentages)):
        left.append(value)
    # plotting a bar chart
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, m_percentages, width, color=['blue'], label='Men')
    rects2 = ax.bar(x + width / 2, f_percentages, width, color=['pink'], label='Women')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Percentage')
    ax.set_title('Percentage by topic and gender')
    ax.set_xticks(x, labels)
    ax.legend()
    plt.xticks(rotation=45)

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()


def reverse_string_array(array):
    output = []
    for s in array:
        reverse_s = s[::-1]
        output.append(reverse_s)
    return output


max_num_of_topics = 30
sum_of_topic_doc_K17_m = [.0] * max_num_of_topics
sum_of_topic_doc_K17_f = [.0] * max_num_of_topics
sum_of_topic_doc_K18_m = [.0] * max_num_of_topics
sum_of_topic_doc_K18_f = [.0] * max_num_of_topics
sum_of_topic_doc_K20_m = [.0] * max_num_of_topics
sum_of_topic_doc_K20_f = [.0] * max_num_of_topics
path = "./{}_document-topic-distribution.csv"
knesset = ["K17", "K18", "K20"]
for knessetNum in knesset:
    csv_path = path.format(knessetNum)
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i = 0
        for row in spamreader:
            string = row[0]
            split = string.split(";")
            if i == 0:
                i += 1
                continue
            split_file_name = split[0].split("_")
            for j in range(1, max_num_of_topics + 1):
                fl = float(split[j])
                if split_file_name[0] == "K17":
                    if split_file_name[1] == "m":
                        sum_of_topic_doc_K17_m[j - 1] += fl
                    else:
                        sum_of_topic_doc_K17_f[j - 1] += fl
                elif split_file_name[0] == "K18":
                    if split_file_name[1] == "m":
                        sum_of_topic_doc_K18_m[j - 1] += fl
                    else:
                        sum_of_topic_doc_K18_f[j - 1] += fl
                else:
                    if split_file_name[1] == "m":
                        sum_of_topic_doc_K20_m[j - 1] += fl
                    else:
                        sum_of_topic_doc_K20_f[j - 1] += fl

percentages_K17_m = []
percentages_K17_f = []
percentages_K18_m = []
percentages_K18_f = []
percentages_K20_m = []
percentages_K20_f = []
sumAll_K17_m = 0
sumAll_K17_f = 0
sumAll_K18_m = 0
sumAll_K18_f = 0
sumAll_K20_m = 0
sumAll_K20_f = 0
for i in range(max_num_of_topics):
    sumAll_K17_m = sumAll_K17_m + sum_of_topic_doc_K17_m[i]
for i in range(max_num_of_topics):
    sumAll_K17_f = sumAll_K17_f + sum_of_topic_doc_K17_f[i]
for i in range(max_num_of_topics):
    sumAll_K18_m = sumAll_K18_m + sum_of_topic_doc_K18_m[i]
for i in range(max_num_of_topics):
    sumAll_K18_f = sumAll_K18_f + sum_of_topic_doc_K18_f[i]
for i in range(max_num_of_topics):
    sumAll_K20_m = sumAll_K20_m + sum_of_topic_doc_K20_m[i]
for i in range(max_num_of_topics):
    sumAll_K20_f = sumAll_K20_f + sum_of_topic_doc_K20_f[i]

for i in range(max_num_of_topics):
    d = sum_of_topic_doc_K17_m[i] / sumAll_K17_m * 100
    percentages_K17_m.append(d)
for i in range(max_num_of_topics):
    d = sum_of_topic_doc_K17_f[i] / sumAll_K17_f * 100
    percentages_K17_f.append(d)
for i in range(max_num_of_topics):
    d = sum_of_topic_doc_K18_m[i] / sumAll_K18_m * 100
    percentages_K18_m.append(d)
for i in range(max_num_of_topics):
    d = sum_of_topic_doc_K18_f[i] / sumAll_K18_f * 100
    percentages_K18_f.append(d)
for i in range(max_num_of_topics):
    d = sum_of_topic_doc_K20_m[i] / sumAll_K20_m * 100
    percentages_K20_m.append(d)
for i in range(max_num_of_topics):
    d = sum_of_topic_doc_K20_f[i] / sumAll_K20_f * 100
    percentages_K20_f.append(d)

k17_topics = ["מינוי בכירים",
              "שיכון ובינוי",
              "זכויות עובדים",
              "פלילים",
              "בנקאות",
              "אלימות במשפחה",
              "זכויות נשים",
              "צרכנות",
              "קצבאות ותגמולים",
              "דת ומדינה",
              "תקשורת",
              "זכויות אדם",
              "תכנון ובנייה",
              "משפחה וילדים",
              "תחבורה",
              "בריאות",
              "שיוויון מגדרי",
              "איכות הסביבה",
              "אנרגיה",
              "בחירות",
              "בטחון וצבא",
              "עלייה וקליטה",
              "חינוך",
              "דיור ונדלן"]
k17_merge_topics = [(3, 24), (18, 29)]
k17_redundant_topics = [5, 6, 14, 27]

k18_topics = ["תקשורת",
              "מדיניות כלכלית",
              "בנקאות והשקעות",
              "איכות הסביבה",
              "מיסוי ושכר",
              "בטחון פנים",
              "פלילים",
              "תחבורה",
              "שירות צבאי",
              "מעמד אזרחי",
              "פיתוח אזורי",
              "בחירות",
              "זכויות אדם",
              "עבירות מין",
              "תכנון ובנייה",
              "חינוך",
              "מינוי בכירים",
              "מורשת יהודית",
              "דת ומדינה",
              "משפט",
              "קצבאות ותגמולים",
              "זכויות עובדים",
              "דיור ונדלן",
              "בריאות",
              "צרכנות"]

k18_merge_topics = [(4, 18)]
k18_redundant_topics = [6, 9, 16, 22]

k20_topics = ["תכנון ובנייה",
              "תחבורה",
              "משפחה וילדים",
              "שירות צבאי",
              "פלילים",
              "חינוך",
              "בריאות",
              "רווחה",
              "קצבאות ותגמולים",
              "מדיניות כלכלית",
              "תרבות וספורט",
              "זכויות עובדים",
              "זכויות אדם",
              "דיור ונדלן",
              "איכות הסביבה",
              "בנקאות",
              "תעסוקה",
              "צרכנות",
              "תקשורת",
              "בחירות",
              "זכויות נשים",
              "משפט",
              "דת ומדינה"]
k20_merge_topics = [(5, 26), (15, 19), (17, 20)]
k20_redundant_topics = [4, 10, 13, 18]

create_plot(percentages_K17_m, percentages_K17_f, reverse_string_array(k17_topics), k17_merge_topics,
            k17_redundant_topics)
create_plot(percentages_K18_m, percentages_K18_f, reverse_string_array(k18_topics), k18_merge_topics,
            k18_redundant_topics)
create_plot(percentages_K20_m, percentages_K20_f, reverse_string_array(k20_topics), k20_merge_topics,
            k20_redundant_topics)

# create_plot(percentages_K17_m, reverse_string_array(k17_topics), k17_merge_topics, k17_redundant_topics, True)
# create_plot(percentages_K17_f, reverse_string_array(k17_topics), k17_merge_topics, k17_redundant_topics, False)
# create_plot(percentages_K18_m, reverse_string_array(k18_topics), k18_merge_topics, k18_redundant_topics, True)
# create_plot(percentages_K18_f, reverse_string_array(k18_topics), k18_merge_topics, k18_redundant_topics, False)
# create_plot(percentages_K20_m, reverse_string_array(k20_topics), k20_merge_topics, k20_redundant_topics, True)
# create_plot(percentages_K20_f, reverse_string_array(k20_topics), k20_merge_topics, k20_redundant_topics, False)

# left = []
# for value in range(num_of_topics):
#     left.append(value)
#
# # labels for bars
# tick_label = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",
#               "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29"]
#
# # plotting a bar chart
# plt.bar(left, percentages, tick_label=tick_label,
#         width=0.8, color=['pink'])
#
# plt.xticks(rotation=45)
#
# # naming the x-axis
# plt.xlabel('x - Topic')
# # naming the y-axis
# plt.ylabel('y - Percentage')
#
# plt.tight_layout()
#
# # function to show the plot
# plt.show()
