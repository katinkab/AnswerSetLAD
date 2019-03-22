after correcting Support.py

_________________________________________________________

Greedy.py (mu=10)

katinka@Korbinian:~$ time python Schreibtisch/AnswerSetLAD/SupportSets/Greedy.py Schreibtisch/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint_nointerval/breastcancerwis_disjoint_suppcalc_new.csv Schreibtisch/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint_nointerval/breastcancerwis_classes_disjoint.csv Schreibtisch/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint_nointerval/breastcancerwis_keepcolumns_mu10.txt
--- feature selection
 input file: Schreibtisch/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint_nointerval/breastcancerwis_disjoint_suppcalc_new.csv
  _suppcalc.csv - number of rows: 50268
  _suppcalc.csv - number of columns: 72
  _classes.csv - number of rows: 449
  _classes.csv - number of columns: 9
--- columns to keep:
   71
   70
   69
   68
   39
   38
   67
   30
   37
   15
   63
   36
   66
   62
   14
   23
   29
   61
   55
   60
   28
   44
   35
   54
   53
   45
   52
   59
   65
   7
   20
   12
   21
   19
   27
   0
--- done.

real	18m3.965s
user	7m35.321s
sys	0m0.884s

_________________________________________________________

Disjoint.py

katinka@Korbinian:~$ time python Schreibtisch/AnswerSetLAD/DataBinarization/Disjoint.py Schreibtisch/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint_nointerval/breastcancerwis_short_new.csv Schreibtisch/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint_nointerval/breastcancerwis_short_new_disjoint.csv
--- remove duplicates
 input file: Schreibtisch/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint_nointerval/breastcancerwis_short_new.csv
  _classes.csv - number of rows: 449
  _classes.csv - number of columns: 36
  no repetition - number of rows: 257
  no repetition - number of columns: 36
  disjoint - number of rows: 249
  disjoint - number of columns: 36
--- done.

real	0m0.245s
user	0m0.502s
sys	0m0.765s

___________________________________________________________

MakeDataFile.py (-> .asp)

katinka@Korbinian:~$ time python Schreibtisch/AnswerSetLAD/MakeDataFile.py Schreibtisch/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint_nointerval/new_correctedSupport/breastcancerwis_short_new_disjoint.csv Schreibtisch/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint_nointerval/new_correctedSupport/breastcancerwis_short_new_disjoint.asp
--- txt2asp
 input file: Schreibtisch/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint_nointerval/new_correctedSupport/breastcancerwis_short_new_disjoint.csv
 number of observations:  249
 number of features:  36
 output file: Schreibtisch/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint_nointerval/new_correctedSupport/breastcancerwis_short_new_disjoint.asp
---

real	0m0.028s
user	0m0.024s
sys	0m0.004s


