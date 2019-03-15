Disjoint.py

katinkab@turing:~$ python 2018-2019/AnswerSetLAD/DataBinarization/Disjoint.py 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/heartdiseasecleveland_classes.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/heartdiseasecleveland_classes_disjoint.csv
--- remove duplicates
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/heartdiseasecleveland_classes.csv
  _classes.csv - number of rows: 297
  _classes.csv - number of columns: 13
  no repetition - number of rows: 297
  no repetition - number of columns: 13
  disjoint - number of rows: 297
  disjoint - number of columns: 13
--- done.

_______________________________________________________

BinarizeData.py (no interval variables)

katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/DataBinarization/BinarizeData.py 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/heartdiseasecleveland_classes_disjoint.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/heartdiseasecleveland_disjoint_binary_nointerval.csv
--- binarize
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/heartdiseasecleveland_classes_disjoint.csv
  number of rows: 297
  number of columns: 13
 
 binary output file: 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/heartdiseasecleveland_disjoint_binary_nointerval.csv
  number of rows: 297
  number of columns: 305
---

real	0m0.910s
user	0m0.624s
sys	0m0.260s


________________________________________________________

Support.py

katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/SupportSets/Support.py 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/heartdiseasecleveland_disjoint_binary_nointerval.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/heartdiseasecleveland_disjoint_suppcalc.csv
--- calculate support matrix
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/heartdiseasecleveland_disjoint_binary_nointerval.csv
  number of rows: 297
  number of columns: 305
name:  heartdiseasecleveland
  suppdata number of rows: 10303
  suppdata number of cols: 305

real	3m2.869s
user	2m26.380s
sys	0m35.872s

_______________________________________________________

Greedy.py (mu = 5)

