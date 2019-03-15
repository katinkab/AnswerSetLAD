Disjoint.py

katinkab@turing:~$ python 2018-2019/AnswerSetLAD/DataBinarization/Disjoint.py 2018-2019/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/breastcancerwis_classes.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/breastcancerwis_classes_disjoint.csv
--- remove duplicates
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/breastcancerwis_classes.csv
  _classes.csv - number of rows: 683
  _classes.csv - number of columns: 9
  no repetition - number of rows: 449
  no repetition - number of columns: 9
  disjoint - number of rows: 449
  disjoint - number of columns: 9
--- done.

_____________________________________________

BinarizeData.py (no interval variables)

katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/DataBinarization/BinarizeData.py 2018-2019/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/breastcancerwis_classes_disjoint.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/breastcancerwis_binary_disjoint_nointerval.csv 
--- binarize
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/breastcancerwis_classes_disjoint.csv
  number of rows: 449
  number of columns: 10
 
 binary output file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/breastcancerwis_binary_disjoint_nointerval.csv
  number of rows: 449
  number of columns: 73
---

real	0m0.725s
user	0m0.452s
sys	0m0.196s

_____________________________________________

Support.py

katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/SupportSets/Support.py 2018-2019/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint/breastcancerwis_binary_disjoint_nointerval.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint/breastcancerwis_disjoint_suppcalc.csv
--- binarize
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint/breastcancerwis_binary_disjoint_nointerval.csv
  number of rows: 449
  number of columns: 72
name:  2018-2019/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint/breastcancerwis
  suppdata number of rows: 27416
  suppdata number of cols: 72

real	3m38.413s
user	2m53.520s
sys	0m44.816s

____________________________________________


Greedy.py (mu = 5) -> 17 features selected

katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/SupportSets/Greedy.py 2018-2019/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint/breastcancerwis_disjoint_suppcalc.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint/breastcancerwis_classes_disjoint.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint/breastcancerwis_greedyout.txt
--- feature selection
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint/breastcancerwis_disjoint_suppcalc.csv
  _suppcalc.csv - number of rows: 27416
  _suppcalc.csv - number of columns: 72
  _classes.csv - number of rows: 449
  _classes.csv - number of columns: 9
 name:  breastcancerwis_disjoint
--- columns to keep:
   71
   70
   69
   68
   39
   38
   67
   37
   30
   66
   36
   15
   35
   28
   34
   0
   44
--- done.

real	3m31.329s
user	3m30.472s
sys	0m0.460s

