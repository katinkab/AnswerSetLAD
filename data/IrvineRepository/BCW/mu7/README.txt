Greedy (mu=7)

katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/SupportSets/Greedy.py 2018-2019/AnswerSetLAD/data/IrvineRepository/BCW/bcw_suppcalc.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/BCW/bcw_classes.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/BCW/mu7/bcw_keepcols7.txt 7
--- feature selection
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BCW/bcw_suppcalc.csv
 mu = 7
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
   66
   36
   63
   29
   55
   60
   53
   28
   65
   44
   20
   7
   27
--- done.

real	6m59.189s
user	6m58.808s
sys	0m0.332s
-----------------------------------

primecover.asp (not optimal, nach etwa 20 std)

Answer: 3
primecover(8,1,1) primecover(9,1,1) primecover(10,1,1) primecover(11,1,1) primecover(47,1,2) primecover(1,1,3) primecover(4,1,4) primecover(20,0,5) primecover(176,0,5) primecover(332,0,5) primecover(25,0,6) primecover(4,0,8)
Optimization: 12

____________________________________________________

primecover_highocc.asp (not optimal, nach etwa 20 std)

Answer: 200
primecover(6,1,1) primecover(8,1,1) primecover(10,1,1) primecover(11,1,1) primecover(45,1,2) primecover(1,1,3) primecover(5,1,4) primecover(349,0,5) primecover(1,0,6) primecover(130,0,6) primecover(163,0,6) primecover(21,0,7)
Optimization: 12 4570037

-----------------------------------

primecover.asp predict: 96,0 %

katinkab@turing:~$ ./Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo 2018-2019/AnswerSetLAD/data/IrvineRepository/BCW/mu7/test_last150.asp 2018-2019/AnswerSetLAD/data/IrvineRepository/BCW/mu7/primecover.asp 2018-2019/AnswerSetLAD/AnswerSetLAD_predict.asp 
clingo version 4.5.4
Reading from ...ineRepository/BCW/mu7/test_last150.asp ...

Solving...
Answer: 1
correctpos(63,of(66)) correctneg(82,of(85)) falsepos(3,of(85)) falseneg(3,of(66))
SATISFIABLE

Models       : 1     
Calls        : 1
Time         : 0.067s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
CPU Time     : 0.060s

--------------------------------
primecover_highocc.asp predict: 96,7 %

katinkab@turing:~$ ./Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo 2018-2019/AnswerSetLAD/data/IrvineRepository/BCW/mu7/test_last150.asp 2018-2019/AnswerSetLAD/data/IrvineRepository/BCW/mu7/primecover_highocc.asp 2018-2019/AnswerSetLAD/AnswerSetLAD_predict.asp 
clingo version 4.5.4

Solving...
Answer: 1
correctpos(64,of(66)) correctneg(82,of(85)) falsepos(3,of(85)) falseneg(2,of(66))
SATISFIABLE

Models       : 1     
Calls        : 1
Time         : 0.074s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
CPU Time     : 0.070s



