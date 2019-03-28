katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/SupportSets/Greedy.py 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/bld_suppcalc.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/bld_classes.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/bld_keepcols5.txt 5
--- feature selection
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/bld_suppcalc.csv
 mu = 5
  _suppcalc.csv - number of rows: 28258
  _suppcalc.csv - number of columns: 269
  _classes.csv - number of rows: 341
  _classes.csv - number of columns: 6
--- columns to keep:
   268
   0
   267
   266
   265
   1
   264
   2
   263
   21
   181
   262
   3
   261
   20
--- done.

real	12m16.117s
user	12m14.896s
sys	0m0.824s

__________________________________________________________


katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/SupportSets/PickFeatures_Greedy.py 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/bld_binary.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/mu5/bld_keepcols5.txt 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/mu5/bld_short.csv
--- write small binary file
 from input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/bld_binary.csv
 and support set: 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/mu5/bld_keepcols5.txt
  number of rows: 341
  number of columns: 269

real	0m0.550s
user	0m0.348s
sys	0m0.248s


__________________________________________________________

Disjoint

katinkab@turing:~$ python 2018-2019/AnswerSetLAD/DataBinarization/Disjoint.py 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/mu5/bld_short.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/mu5/bld_short_disjoint.csv
--- remove duplicates
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/mu5/bld_short.csv
  _classes.csv - number of rows: 341
  _classes.csv - number of columns: 15
  no repetition - number of rows: 31
  no repetition - number of columns: 15
  disjoint - number of rows: 15
  disjoint - number of columns: 15
--- done.
---------------------------------------------------------------

train disjoint

katinkab@turing:~$ python 2018-2019/AnswerSetLAD/DataBinarization/Disjoint.py 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/mu5/train_first228.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/mu5/train_disjoint.csv
--- remove duplicates
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/mu5/train_first228.csv
  _classes.csv - number of rows: 226
  _classes.csv - number of columns: 15
  no repetition - number of rows: 25
  no repetition - number of columns: 15
  disjoint - number of rows: 13
  disjoint - number of columns: 15
--- done.

---------------------------------------------------------------

katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/allpatterns.py 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/mu5/train_disjoint.asp 2018-2019/AnswerSetLAD/AnswerSetLAD_prime.asp 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/mu5/allprimes.txt 1 15 100 0
--- getallpatterns starts calculating...
 data file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/mu5/train_disjoint.asp
 patterns calculated with: 2018-2019/AnswerSetLAD/AnswerSetLAD_prime.asp
 lower bound degree: 1
 upper bound degree: 15
 homogeneity in percent (lower bound): 100
 prevalence in percent (lower bound): 0
	output file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/mu5/allprimes.txt

 positive patterns:
...done...
 negative patterns:
--- getallpatterns done. 

real	0m0.475s
user	0m0.284s
sys	0m0.028s

------------------------------------------------------------

primecover

katinkab@turing:~$ time ./Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/mu5/train_disjoint.asp 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/mu5/allprimes_forcover.asp 2018-2019/AnswerSetLAD/AnswerSetLAD_primecover.asp 
clingo version 4.5.4
Reading from ...eRepository/BLD/mu5/train_disjoint.asp ...
Solving...
Answer: 1
primecover(1,1,1) primecover(1,1,2) primecover(2,1,2) primecover(3,1,4) primecover(1,0,1) primecover(3,0,1) primecover(3,0,2) primecover(11,0,2) primecover(13,0,3)
Optimization: 9
OPTIMUM FOUND

Models       : 1     
  Optimum    : yes
Optimization : 9
Calls        : 1
Time         : 0.019s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
CPU Time     : 0.000s

real	0m0.023s
user	0m0.008s
sys	0m0.004s
________________________________________________

primecover_highocc

katinkab@turing:~$ time ./Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/mu5/train_disjoint.asp 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/mu5/allprimes_forcover.asp 2018-2019/AnswerSetLAD/AnswerSetLAD_primecover_highoccurence.asp 
clingo version 4.5.4
Solving...
..
Answer: 8
primecover(1,1,1) primecover(1,1,2) primecover(3,1,4) primecover(6,1,4) primecover(1,0,1) primecover(3,0,1) primecover(3,0,2) primecover(12,0,2) primecover(10,0,3)
Optimization: 9 193
OPTIMUM FOUND

Models       : 8     
  Optimum    : yes
Optimization : 9 193
Calls        : 1
Time         : 0.055s (Solving: 0.01s 1st Model: 0.00s Unsat: 0.00s)
CPU Time     : 0.020s

real	0m0.061s
user	0m0.024s
sys	0m0.000s

--------------------------------------------

test not disjoint (weil egal)

katinkab@turing:~$ python 2018-2019/AnswerSetLAD/MakeDataFile.py 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/mu5/test_last114.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/mu5/test_last114.asp
--- txt2asp
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/mu5/test_last114.csv
 number of observations:  115
 number of features:  15
 output file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/mu5/test_last114.asp
---

__________________________________________

predict:

primecover: 73,33 %
Answer: 1
correctpos(3,of(40)) correctneg(74,of(75)) falsepos(1,of(75)) falseneg(37,of(40))
SATISFIABLE

Models       : 1     
Calls        : 1
Time         : 0.028s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
CPU Time     : 0.020s


primecover_highocc: 78,1 %
Answer: 1
correctpos(20,of(40)) correctneg(62,of(75)) falsepos(13,of(75)) falseneg(20,of(40))
SATISFIABLE

Models       : 1     
Calls        : 1
Time         : 0.029s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
CPU Time     : 0.020s




