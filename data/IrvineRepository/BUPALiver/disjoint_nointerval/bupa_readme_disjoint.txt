Disjoint.py

katinkab@turing:~$ python 2018-2019/AnswerSetLAD/DataBinarization/Disjoint.py 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/bupa_classes.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/bupa_classes_disjoint.csv
--- remove duplicates
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/bupa_classes.csv
  _classes.csv - number of rows: 345
  _classes.csv - number of columns: 6
  no repetition - number of rows: 341
  no repetition - number of columns: 6
  disjoint - number of rows: 341
  disjoint - number of columns: 6
--- done.

________________________________________________________________


BinarizeData.py (no interval variables)

katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/DataBinarization/BinarizeData.py 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/bupa_classes_disjoint.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/bupa_binary.csv
--- binarize
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/bupa_classes_disjoint.csv
  number of rows: 341
  number of columns: 6
 
 binary output file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/bupa_binary.csv
  number of rows: 341
  number of columns: 269
---

real	0m0.870s
user	0m0.660s
sys	0m0.248s

________________________________________________________________

Support.py

katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/SupportSets/Support.py 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/bupa_binary.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/bupa_suppcalc_disjoint.csv
--- calculate support matrix
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/bupa_binary.csv
  number of rows: 341
  number of columns: 269
  suppdata number of rows: 15301
  suppdata number of cols: 269

real	4m45.381s
user	3m34.572s
sys	1m10.544s

________________________________________________________________

Greedy.py (mu = 5) -> 14 features selected

katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/SupportSets/Greedy.py 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/bupa_suppcalc_disjoint.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/bupa_classes_disjoint.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/bupa_disjoint_keepcolumns.txt
--- feature selection
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/bupa_suppcalc_disjoint.csv
  _suppcalc.csv - number of rows: 15301
  _suppcalc.csv - number of columns: 269
  _classes.csv - number of rows: 341
  _classes.csv - number of columns: 6
--- columns to keep:
   268
   267
   0
   266
   265
   264
   1
   263
   2
   21
   181
   262
   20
   261
--- done.

real	6m49.042s
user	6m47.588s
sys	0m0.752s


________________________________________________________________

Greedy.py (mu = 10) -> 44 features selected

katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/SupportSets/Greedy.py 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/bupa_suppcalc_disjoint.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/bupa_classes_disjoint.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/bupa_disjoint_keepcolumns.txt
--- feature selection
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/bupa_suppcalc_disjoint.csv
  _suppcalc.csv - number of rows: 15301
  _suppcalc.csv - number of columns: 269
  _classes.csv - number of rows: 341
  _classes.csv - number of columns: 6
--- columns to keep:
   268
   267
   0
   266
   265
   1
   264
   2
   263
   21
   181
   3
   20
   180
   262
   19
   4
   261
   18
   5
   90
   260
   179
   145
   17
   178
   89
   6
   259
   177
   16
   88
   7
   176
   144
   258
   15
   175
   256
   8
   257
   174
   14
   146
--- done.

real	9m59.515s
user	9m58.644s
sys	0m0.432s

_______________________________________________________________

PickFeatures.py (from _mu5)

katinkab@turing:~$ python 2018-2019/AnswerSetLAD/SupportSets/PickFeatures_Greedy.py 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/bupa_binary_disjointnointerval.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/bupa_disjoint_keepcolumns_mu5.txt 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/bupa_short_binary.txt
--- write small binary file
 from input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/bupa_binary_disjointnointerval.csv
 and support set: 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/bupa_disjoint_keepcolumns_mu5.txt
  number of rows: 341
  number of columns: 269

_______________________________________________________________

Disjoint.py (-> bupa_final.csv)

katinkab@turing:~$ python 2018-2019/AnswerSetLAD/DataBinarization/Disjoint.py 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/bupa_short_binary.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/bupa_final.csv
--- remove duplicates
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/bupa_short_binary.csv
  _classes.csv - number of rows: 341
  _classes.csv - number of columns: 14
  no repetition - number of rows: 29
  no repetition - number of columns: 14
  disjoint - number of rows: 15
  disjoint - number of columns: 14
--- done.




