PickFeatures_Greedy.py (von mu=5)

katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/SupportSets/PickFeatures_Greedy.py 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/heartdiseasecleveland_disjoint_binary_nointerval.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/new_correctedsupport/heartdisease_keepcolumns5_new.txt 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/new_correctedsupport/heartdisease_short_mu5.csv
--- write small binary file
 from input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/heartdiseasecleveland_disjoint_binary_nointerval.csv
 and support set: 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/new_correctedsupport/heartdisease_keepcolumns5_new.txt
  number of rows: 297
  number of columns: 305

real	0m0.533s
user	0m0.264s
sys	0m0.232s

__________________________________________________

Disjoint.py

katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/DataBinarization/Disjoint.py 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/new_correctedsupport/mu5/heartdisease_short_mu5.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/new_correctedsupport/mu5/heartdisease_short_mu5_disjoint.csv
--- remove duplicates
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/new_correctedsupport/mu5/heartdisease_short_mu5.csv
  _classes.csv - number of rows: 297
  _classes.csv - number of columns: 14
  no repetition - number of rows: 147
  no repetition - number of columns: 14
  disjoint - number of rows: 105
  disjoint - number of columns: 14
--- done.

real	0m0.551s
user	0m0.256s
sys	0m0.236s

_________________________________________________

MakeDataFile.py

katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/MakeDataFile.py 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/new_correctedsupport/mu5/heartdisease_short_mu5_disjoint.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/new_correctedsupport/mu5/heartdisease_short_mu5_disjoint.asp
--- txt2asp
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/new_correctedsupport/mu5/heartdisease_short_mu5_disjoint.csv
 number of observations:  105
 number of features:  14
 output file: 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/new_correctedsupport/mu5/heartdisease_short_mu5_disjoint.asp
---

real	0m0.014s
user	0m0.008s
sys	0m0.000s


