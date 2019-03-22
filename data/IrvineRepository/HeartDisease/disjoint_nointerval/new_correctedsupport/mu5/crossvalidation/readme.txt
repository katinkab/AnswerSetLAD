allpatterns.py

katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/allpatterns.py 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/new_correctedsupport/mu5/crossvalidation/trainset_first70.asp 2018-2019/AnswerSetLAD/AnswerSetLAD_prime.asp 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/new_correctedsupport/mu5/crossvalidation/allprimes.txt 1 14 100 0
--- getallpatterns starts calculating...
 data file: 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/new_correctedsupport/mu5/crossvalidation/trainset_first70.asp
 patterns calculated with: 2018-2019/AnswerSetLAD/AnswerSetLAD_prime.asp
 lower bound degree: 1
 upper bound degree: 14
 homogeneity in percent (lower bound): 100
 prevalence in percent (lower bound): 0
	output file: 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/new_correctedsupport/mu5/crossvalidation/allprimes.txt

 positive patterns:
...done...
 negative patterns:
--- getallpatterns done. 

real	0m1.822s
user	0m1.724s
sys	0m0.052s

____________________________________________

ReadAllPatternsForCoverCalc.py

katinkab@turing:~$ time python 2018-2019/AnswerSetLAD/ReadAllPatternForCoverCalc.py 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/new_correctedsupport/mu5/crossvalidation/allprimes.txt 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/new_correctedsupport/mu5/crossvalidation/allprimes_forcover.asp
--- patternoutput_to_coverinput
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/new_correctedsupport/mu5/crossvalidation/allprimes.txt
 output file: 2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/new_correctedsupport/mu5/crossvalidation/allprimes_forcover.asp
---

real	0m0.016s
user	0m0.016s
sys	0m0.000s

____________________________________________

primecover.asp





