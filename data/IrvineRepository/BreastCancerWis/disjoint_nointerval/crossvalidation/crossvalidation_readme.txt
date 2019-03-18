allpatterns.py -> calculate all prime patterns (save as allprimes.txt)

katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/allpatterns.py 2018-2019/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint_nointerval/crossvalidation/trainset_first404obs.asp 2018-2019/AnswerSetLAD/AnswerSetLAD_prime.asp 1 17 100 0 quiet 
--- getallpatterns starts calculating...
 data file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint_nointerval/crossvalidation/trainset_first404obs.asp
 patterns calculated with: 2018-2019/AnswerSetLAD/AnswerSetLAD_prime.asp
 lower bound degree: 1
 upper bound degree: 17
 homogeneity in percent (lower bound): 100
 prevalence in percent (lower bound): 0

 positive patterns:
  degree 1: Models       : 3

  degree 2: Models       : 62

  degree 3: Models       : 10

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

  degree 15: Models       : 0

  degree 16: Models       : 0

  degree 17: Models       : 0


 negative patterns:
  degree 1: Models       : 0

  degree 2: Models       : 8

  degree 3: Models       : 4

  degree 4: Models       : 5

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

  degree 15: Models       : 0

  degree 16: Models       : 0

  degree 17: Models       : 0

--- getallpatterns done. 

real	0m13.215s
user	0m12.816s
sys	0m0.248s

_____________________________________________________________

ReadAllPatternForCoverCalc.py (-> allprimes_forcover.asp)

katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/ReadAllPatternForCoverCalc.py 2018-2019/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint_nointerval/crossvalidation/allprimes.txt 2018-2019/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint_nointerval/crossvalidation/allprimes_forcover.asp
--- patternoutput_to_coverinput
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint_nointerval/crossvalidation/allprimes.txt
 output file: 2018-2019/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/disjoint_nointerval/crossvalidation/allprimes_forcover.asp
---

real	0m0.033s
user	0m0.020s
sys	0m0.008s

_____________________________________________________________






