This folder contains selected files from the original HeartDisease folder.

- hd_classes.csv: disjoint
- hd_binary.csv: only level variables
- hd_suppcalc.csv: with corrected Support.py

_____________________________________________

mu3/

Greedy.py (mu=3)

katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/SupportSets/Greedy.py 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/hd_suppcalc.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/hd_classes.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu3/hd_keepcolumns3.txt
--- feature selection
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/hd_suppcalc.csv
  _suppcalc.csv - number of rows: 21920
  _suppcalc.csv - number of columns: 305
  _classes.csv - number of rows: 297
  _classes.csv - number of columns: 13
--- columns to keep:
   196
   37
   266
   299
   302
   298
   38
   197
--- done.

real	9m8.388s
user	9m5.740s
sys	0m0.584s

____________________________________________

PickFeatures_Greedy.py

katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/SupportSets/PickFeatures_Greedy.py 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/hd_binary.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu3/hd_keepcolumns3.txt 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu3/hd_short.csv
--- write small binary file
 from input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/hd_binary.csv
 and support set: 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu3/hd_keepcolumns3.txt
  number of rows: 297
  number of columns: 305

real	0m0.480s
user	0m0.292s
sys	0m0.252s

________________________________________________

Disjoint.py (-> short_disjoint.csv)

katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/DataBinarization/Disjoint.py 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu3/hd_short.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu3/hd_short_disjoint.csv
--- remove duplicates
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu3/hd_short.csv
  _classes.csv - number of rows: 297
  _classes.csv - number of columns: 8
  no repetition - number of rows: 87
  no repetition - number of columns: 8
  disjoint - number of rows: 49
  disjoint - number of columns: 8
--- done.

real	0m0.721s
user	0m0.364s
sys	0m0.292s

_____________________________________________

allpatterns.py

katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/allpatterns.py 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu3/train_first33.asp 2018-2019/AnswerSetLAD/AnswerSetLAD_prime.asp 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu3/allprimes.txt 1 8 100 0
--- getallpatterns starts calculating...
 data file: 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu3/train_first33.asp
 patterns calculated with: 2018-2019/AnswerSetLAD/AnswerSetLAD_prime.asp
 lower bound degree: 1
 upper bound degree: 8
 homogeneity in percent (lower bound): 100
 prevalence in percent (lower bound): 0
	output file: 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu3/allprimes.txt

 positive patterns:
...done...
 negative patterns:
--- getallpatterns done. 

real	0m0.342s
user	0m0.188s
sys	0m0.016s

______________________________________________

ReadAll....

katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/ReadAllPatternForCoverCalc.py 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu3/allprimes.txt 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu3/allprimes_forcover.asp
--- patternoutput_to_coverinput
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu3/allprimes.txt
 output file: 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu3/allprimes_forcover.asp
---

real	0m0.022s
user	0m0.004s
sys	0m0.012s

_______________________________________________
_______________________________________________

primecover.asp

katinkab@turing:~$ time ./Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu3/train_first33.asp 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu3/allprimes_forcover.asp 2018-2019/AnswerSetLAD/AnswerSetLAD_primecover.asp 
clingo version 4.5.4
Reading from ...ineRepository/HD/mu3/train_first33.asp ...
Solving...
Answer: 1
primecover(2,1,3) primecover(4,1,3) primecover(8,1,3) primecover(2,1,4) primecover(12,1,4) primecover(21,1,4) primecover(32,1,4) primecover(1,0,1) primecover(2,0,2) primecover(3,0,2) primecover(6,0,3) primecover(8,0,4) primecover(11,0,4)
Optimization: 13
Answer: 2
primecover(1,1,3) primecover(4,1,3) primecover(6,1,4) primecover(12,1,4) primecover(21,1,4) primecover(32,1,4) primecover(1,0,1) primecover(2,0,2) primecover(3,0,2) primecover(6,0,3) primecover(8,0,4) primecover(11,0,4)
Optimization: 12
OPTIMUM FOUND

Models       : 2     
  Optimum    : yes
Optimization : 12
Calls        : 1
Time         : 0.279s (Solving: 0.26s 1st Model: 0.00s Unsat: 0.26s)
CPU Time     : 0.270s

real	0m0.284s
user	0m0.276s
sys	0m0.000s

----------------------------------------------

primecover_highoccurence.asp

katinkab@turing:~$ time ./Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu3/train_first33.asp 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu3/allprimes_forcover.asp 2018-2019/AnswerSetLAD/AnswerSetLAD_primecover_highoccurence.asp 
clingo version 4.5.4
Reading from ...ineRepository/HD/mu3/train_first33.asp ...
Solving...
Answer: 1
primecover(11,1,3) primecover(2,1,4) primecover(12,1,4) primecover(16,1,4) primecover(20,1,4) primecover(23,1,4) primecover(1,0,1) primecover(2,0,2) primecover(3,0,2) primecover(6,0,3) primecover(8,0,4) primecover(9,0,4)
Optimization: 12 4206
Answer: 2
primecover(1,1,3) primecover(11,1,3) primecover(6,1,4) primecover(12,1,4) primecover(16,1,4) primecover(24,1,4) primecover(1,0,1) primecover(2,0,2) primecover(3,0,2) primecover(6,0,3) primecover(8,0,4) primecover(9,0,4)
Optimization: 12 4169
Answer: 3
primecover(1,1,3) primecover(11,1,3) primecover(2,1,4) primecover(12,1,4) primecover(18,1,4) primecover(23,1,4) primecover(1,0,1) primecover(2,0,2) primecover(3,0,2) primecover(6,0,3) primecover(8,0,4) primecover(9,0,4)
Optimization: 12 4125
Answer: 4
primecover(2,1,3) primecover(2,1,4) primecover(12,1,4) primecover(18,1,4) primecover(23,1,4) primecover(32,1,4) primecover(1,0,1) primecover(1,0,2) primecover(2,0,2) primecover(6,0,3) primecover(11,0,4) primecover(1,0,5)
Optimization: 12 4112
Answer: 5
primecover(2,1,3) primecover(11,1,3) primecover(2,1,4) primecover(12,1,4) primecover(13,1,4) primecover(23,1,4) primecover(1,0,1) primecover(2,0,2) primecover(3,0,2) primecover(6,0,3) primecover(8,0,4) primecover(11,0,4)
Optimization: 12 4101
Answer: 6
primecover(1,1,3) primecover(11,1,3) primecover(2,1,4) primecover(12,1,4) primecover(21,1,4) primecover(23,1,4) primecover(1,0,1) primecover(2,0,2) primecover(3,0,2) primecover(6,0,3) primecover(8,0,4) primecover(11,0,4)
Optimization: 12 4064
Answer: 7
primecover(1,1,3) primecover(2,1,4) primecover(12,1,4) primecover(18,1,4) primecover(23,1,4) primecover(32,1,4) primecover(1,0,1) primecover(1,0,2) primecover(2,0,2) primecover(6,0,3) primecover(11,0,4) primecover(1,0,5)
Optimization: 12 4063
Answer: 8
primecover(1,1,3) primecover(2,1,4) primecover(12,1,4) primecover(16,1,4) primecover(23,1,4) primecover(32,1,4) primecover(1,0,1) primecover(1,0,2) primecover(2,0,2) primecover(6,0,3) primecover(11,0,4) primecover(1,0,5)
Optimization: 12 4058
Answer: 9
primecover(1,1,3) primecover(11,1,3) primecover(2,1,4) primecover(12,1,4) primecover(16,1,4) primecover(23,1,4) primecover(1,0,1) primecover(2,0,2) primecover(3,0,2) primecover(6,0,3) primecover(8,0,4) primecover(11,0,4)
Optimization: 12 4020
Answer: 10
primecover(1,1,3) primecover(2,1,4) primecover(12,1,4) primecover(16,1,4) primecover(23,1,4) primecover(32,1,4) primecover(1,0,1) primecover(2,0,2) primecover(3,0,2) primecover(6,0,3) primecover(11,0,4) primecover(1,0,5)
Optimization: 12 4019
Answer: 11
primecover(1,1,3) primecover(11,1,3) primecover(2,1,4) primecover(12,1,4) primecover(16,1,4) primecover(23,1,4) primecover(1,0,1) primecover(2,0,2) primecover(3,0,2) primecover(6,0,3) primecover(11,0,4) primecover(1,0,5)
Optimization: 12 4000
OPTIMUM FOUND

Models       : 11    
  Optimum    : yes
Optimization : 12 4000
Calls        : 1
Time         : 0.394s (Solving: 0.37s 1st Model: 0.00s Unsat: 0.11s)
CPU Time     : 0.390s

real	0m0.400s
user	0m0.396s
sys	0m0.000s

____________________________________________________
____________________________________________________

primecover.asp

katinkab@turing:~$ ./Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu3/test_last16.asp 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu3/primecover.asp 2018-2019/AnswerSetLAD/AnswerSetLAD_predict.asp 
clingo version 4.5.4
Reading from ...rvineRepository/HD/mu3/test_last16.asp ...

Solving...
Answer: 1
correctpos(5,of(10)) correctneg(5,of(6)) falsepos(1,of(6)) falseneg(5,of(10))
SATISFIABLE

Models       : 1     
Calls        : 1
Time         : 0.017s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
CPU Time     : 0.000s

------------------------------------------

primecover_highocc.asp

katinkab@turing:~$ ./Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu3/test_last16.asp 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu3/primecover_highocc.asp 2018-2019/AnswerSetLAD/AnswerSetLAD_predict.asp 
clingo version 4.5.4
Reading from ...rvineRepository/HD/mu3/test_last16.asp ...

Solving...
Answer: 1
correctpos(4,of(10)) correctneg(5,of(6)) falsepos(1,of(6)) falseneg(6,of(10))
SATISFIABLE

Models       : 1     
Calls        : 1
Time         : 0.011s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
CPU Time     : 0.010s







