<div align="center">
  ניתוח ייצוג מהותי של חברות כנסת

</div>

## Requirements
In order to run this project you will need:
- [Python](https://www.python.org/) as programming language
- [LibreOffice](https://www.libreoffice.org/) for doc to txt convertions
- [LemLDA](https://www.cs.bgu.ac.il/~elhadad/nlpproj/LDAforHebrew.html) for lemmatizing
- [Dariah Topic Explorer](https://dariah-de.github.io/TopicsExplorer/) for topic modeling

## Getting started
Python 3.9 is required

```bash
(1) Download Knesset Odata xlsx of {BillId, KnessetNum, FirstName, LastName, Gender, PathForFile}
(2) Run convertor.py to create convertor_to_txt.sh
(3) Run convertor_to_txt.sh
(4) Trim unrelavent data from text using trimmer.py
(5) Use BGU NLP - LemLDA to extract lemmas
  (5.1) Run "tag ..\..\downloadedFiles ..\..\downloadedFilesTagged"
  (5.2) Run "dot ..\..\downloadedFilesTagged ..\..\downloadedFilesTaggedDotted -lemma"
(6) Run extract_dotted.py to get only lemmes from text files
(7) Run strip_vowels.py to remove dottes
(8) Run Dariah Topic Explorer and export data
(9) Use plot_data_sum.py to plot statistics
(10) run bill2path.py to genarate csv file for close reading
```

## Output
- A plot is created for each Knesset (currently for 17,18,20) for data examination
- KknessetNumber_gender_topic2path is created for close reading 
