allpatterns.py (-> allprimes.txt)

katinkab@turing:~$ python 2018-2019/AnswerSetLAD/allpatterns.py 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/crossvalidation/trainset_first10.asp 2018-2019/AnswerSetLAD/AnswerSetLAD_prime.asp 1 14 100 0
--- getallpatterns starts calculating...
 data file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/crossvalidation/trainset_first10.asp
 patterns calculated with: 2018-2019/AnswerSetLAD/AnswerSetLAD_prime.asp
 lower bound degree: 1
 upper bound degree: 14
 homogeneity in percent (lower bound): 100
 prevalence in percent (lower bound): 0

 positive patterns:
  pat(1,1) covered(1,9)
  pat(7,0) covered(1,10)
  degree 1: Models       : 2

  degree 2: Models       : 0

  pat(13,1) pat(10,0) pat(14,0) covered(1,4)
  degree 3: Models       : 1

  pat(11,0) pat(9,1) pat(10,0) pat(14,0) covered(1,4)
  degree 4: Models       : 1

  degree 5: Models       : 0

  degree 6: Models       : 0

  degree 7: Models       : 0

  degree 8: Models       : 0

  degree 9: Models       : 0

  degree 10: Models       : 0

  degree 11: Models       : 0

  degree 12: Models       : 0

  degree 13: Models       : 0

  degree 14: Models       : 0


 negative patterns:
  pat(11,1) covered(0,1) covered(0,7)
  pat(10,1) covered(0,3) covered(0,6)
  degree 1: Models       : 2

  pat(2,1) pat(1,0) covered(0,8)
  pat(9,0) pat(7,1) covered(0,2)
  pat(8,1) pat(2,0) covered(0,7)
  pat(8,1) pat(1,0) covered(0,7) covered(0,8)
  pat(6,1) pat(2,0) covered(0,7)
  pat(6,1) pat(1,0) covered(0,7) covered(0,8)
  pat(5,1) pat(2,0) covered(0,7)
  pat(5,1) pat(1,0) covered(0,7) covered(0,8)
  pat(4,1) pat(2,0) covered(0,7)
  pat(4,1) pat(1,0) covered(0,7) covered(0,8)
  pat(12,1) pat(5,0) covered(0,6)
  pat(12,1) pat(4,0) covered(0,6)
  pat(12,1) pat(6,0) covered(0,6)
  pat(12,1) pat(1,0) covered(0,6) covered(0,7) covered(0,8)
  pat(12,1) pat(8,0) covered(0,6)
  pat(12,1) pat(2,0) covered(0,6) covered(0,7)
  pat(13,1) pat(12,1) covered(0,6)
  pat(14,1) pat(2,0) covered(0,5) covered(0,6) covered(0,7)
  pat(14,1) pat(5,0) covered(0,5) covered(0,6)
  pat(14,1) pat(4,0) covered(0,5) covered(0,6)
  pat(14,1) pat(6,0) covered(0,5) covered(0,6)
  pat(14,1) pat(8,0) covered(0,5) covered(0,6)
  pat(14,1) pat(12,0) covered(0,5)
  pat(13,1) pat(14,1) covered(0,5) covered(0,6)
  pat(14,1) pat(1,0) covered(0,5) covered(0,6) covered(0,7) covered(0,8)
  degree 2: Models       : 25

  pat(9,1) pat(13,0) pat(1,0) covered(0,1) covered(0,7) covered(0,8)
  pat(13,0) pat(1,0) pat(7,1) covered(0,1) covered(0,2) covered(0,7) covered(0,8)
  pat(9,1) pat(13,0) pat(2,0) covered(0,1) covered(0,7)
  pat(13,0) pat(2,0) pat(7,1) covered(0,1) covered(0,2) covered(0,7)
  pat(9,1) pat(13,0) pat(4,0) covered(0,1)
  pat(13,0) pat(4,0) pat(7,1) covered(0,1) covered(0,2)
  pat(9,1) pat(13,0) pat(8,0) covered(0,1)
  pat(13,0) pat(8,0) pat(7,1) covered(0,1) covered(0,2)
  pat(9,1) pat(13,0) pat(6,0) covered(0,1)
  pat(13,0) pat(6,0) pat(7,1) covered(0,1) covered(0,2)
  pat(9,1) pat(13,0) pat(5,0) covered(0,1)
  pat(13,0) pat(5,0) pat(7,1) covered(0,1) covered(0,2)
  pat(9,1) pat(13,0) pat(12,0) covered(0,1)
  pat(13,0) pat(12,0) pat(7,1) covered(0,1) covered(0,2)
  pat(9,1) pat(13,0) pat(14,0) covered(0,1)
  pat(13,0) pat(14,0) pat(7,1) covered(0,1) covered(0,2)
  degree 3: Models       : 16

  degree 4: Models       : 0

  degree 5: Models       : 0

  degree 6: Models       : 0

  degree 7: Models       : 0

  degree 8: Models       : 0

  degree 9: Models       : 0

  degree 10: Models       : 0

  degree 11: Models       : 0

  degree 12: Models       : 0

  degree 13: Models       : 0

  degree 14: Models       : 0

--- getallpatterns done. 

_______________________________________________________

ReadAllPatternForCoverCalc.py (->allprimes_forcover.txt)

________________________________________________________

PRIMECOVER:

katinkab@turing:~$ time ./Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/crossvalidation/trainset_first10.asp 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/crossvalidation/allprimes_forcover.asp 2018-2019/AnswerSetLAD/AnswerSetLAD_primecover.asp 
clingo version 4.5.4
Reading from ...l/crossvalidation/trainset_first10.asp ...
Solving...
Answer: 1
primecover(1,1,1) primecover(2,1,1) primecover(1,1,4) primecover(2,0,1) primecover(1,0,2) primecover(18,0,2) primecover(16,0,3)
Optimization: 7
Answer: 2
primecover(1,1,1) primecover(2,1,1) primecover(1,1,4) primecover(2,0,1) primecover(25,0,2) primecover(16,0,3)
Optimization: 6
OPTIMUM FOUND

Models       : 2     
  Optimum    : yes
Optimization : 6
Calls        : 1
Time         : 0.010s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
CPU Time     : 0.000s

real	0m0.015s
user	0m0.008s
sys	0m0.008s

_______________________________________________________

PRIMECOVER HIGH OCCURENCE:

katinkab@turing:~$ time ./Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/crossvalidation/trainset_first10.asp 2018-2019/AnswerSetLAD/data/IrvineRepository/BUPALiver/disjoint_nointerval/crossvalidation/allprimes_forcover.asp 2018-2019/AnswerSetLAD/AnswerSetLAD_primecover_highoccurence.asp 
clingo version 4.5.4
Reading from ...l/crossvalidation/trainset_first10.asp ...
2018-2019/AnswerSetLAD/AnswerSetLAD_primecover_highoccurence.asp:23:52-53: info: global variable in tuple of aggregate element:
  S

2018-2019/AnswerSetLAD/AnswerSetLAD_primecover_highoccurence.asp:30:61-62: info: global variable in tuple of aggregate element:
  S

Solving...
Answer: 1
primecover(1,1,1) primecover(2,1,1) primecover(1,1,4) primecover(2,0,1) primecover(2,0,2) primecover(10,0,2) primecover(22,0,2) primecover(15,0,3)
Optimization: 8 100
Answer: 2
primecover(1,1,1) primecover(2,1,1) primecover(1,1,4) primecover(1,0,1) primecover(2,0,1) primecover(2,0,2) primecover(10,0,2) primecover(22,0,2)
Optimization: 8 98
Answer: 3
primecover(1,1,1) primecover(2,1,1) primecover(1,1,4) primecover(2,0,1) primecover(10,0,2) primecover(22,0,2) primecover(16,0,3)
Optimization: 7 109
Answer: 4
primecover(1,1,1) primecover(2,1,1) primecover(1,1,4) primecover(2,0,1) primecover(22,0,2) primecover(1,0,3) primecover(16,0,3)
Optimization: 7 85
Answer: 5
primecover(1,1,1) primecover(2,1,1) primecover(1,1,4) primecover(2,0,1) primecover(2,0,2) primecover(22,0,2) primecover(1,0,3)
Optimization: 7 75
Answer: 6
primecover(1,1,1) primecover(2,1,1) primecover(1,1,4) primecover(2,0,1) primecover(22,0,2) primecover(1,0,3) primecover(2,0,3)
Optimization: 7 51
Answer: 7
primecover(1,1,1) primecover(2,1,1) primecover(1,1,4) primecover(2,0,1) primecover(22,0,2) primecover(2,0,3)
Optimization: 6 75
Answer: 8
primecover(1,1,1) primecover(2,1,1) primecover(1,1,4) primecover(2,0,1) primecover(25,0,2) primecover(2,0,3)
Optimization: 6 66
OPTIMUM FOUND

Models       : 8     
  Optimum    : yes
Optimization : 6 66
Calls        : 1
Time         : 0.013s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
CPU Time     : 0.010s

real	0m0.018s
user	0m0.012s
sys	0m0.004s





