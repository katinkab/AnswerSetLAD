katinkab@turing:~$ python 2018-2019/AnswerSetLAD/MakeDataFile.py 2018-2019/AnswerSetLAD/data/IrvineRepository/H
HD/           HeartDisease/ 
katinkab@turing:~$ python 2018-2019/AnswerSetLAD/DataBinarization/Disjoint.py 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu4/train_first199.csv 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu4/train_short.csv
--- remove duplicates
 input file: 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu4/train_first199.csv
  _classes.csv - number of rows: 197
  _classes.csv - number of columns: 11
  no repetition - number of rows: 87
  no repetition - number of columns: 11
  disjoint - number of rows: 55
  disjoint - number of columns: 11

------------------------------------------------------

primecover.asp

katinkab@turing:~$ time ./Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu4/train_short.asp 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu4/allprimes_forcover.asp 2018-2019/AnswerSetLAD/AnswerSetLAD_primecover.asp 
clingo version 4.5.4
Reading from ...rvineRepository/HD/mu4/train_short.asp ...
Solving...
Answer: 1
...
Answer: 5
primecover(6,1,2) primecover(1,1,4) primecover(9,1,4) primecover(12,1,4) primecover(20,1,4) primecover(35,1,4) primecover(1,0,1) primecover(1,0,2) primecover(3,0,2) primecover(1,0,3) primecover(8,0,3) primecover(13,0,4)
Optimization: 12
OPTIMUM FOUND

Models       : 5     
  Optimum    : yes
Optimization : 12
Calls        : 1
Time         : 16.797s (Solving: 16.77s 1st Model: 0.00s Unsat: 16.75s)
CPU Time     : 16.790s

real	0m16.802s
user	0m16.792s
sys	0m0.004s

---------------------------------

primecover_highocc.asp

Answer: 76
primecover(6,1,2) primecover(4,1,4) primecover(8,1,4) primecover(26,1,4) primecover(35,1,4) primecover(4,1,5) primecover(1,0,1) primecover(1,0,2) primecover(3,0,2) primecover(1,0,3) primecover(5,0,3) primecover(17,0,3)
Optimization: 12 26027
OPTIMUM FOUND

Models       : 76    
  Optimum    : yes
Optimization : 12 26027
Calls        : 1
Time         : 483.509s (Solving: 483.48s 1st Model: 0.00s Unsat: 441.66s)
CPU Time     : 483.470s

real	8m3.518s
user	8m3.272s
sys	0m0.208s


____________________________________________________________

predict primecover.asp: 81%

katinkab@turing:~$ ./Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu4/test_last99.asp 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu4/primecover.asp 2018-2019/AnswerSetLAD/AnswerSetLAD_predict.asp 
clingo version 4.5.4
Reading from ...rvineRepository/HD/mu4/test_last99.asp ...

Solving...
Answer: 1 
correctpos(31,of(47)) correctneg(50,of(53)) falsepos(3,of(53)) falseneg(16,of(47))
SATISFIABLE

Models       : 1     
Calls        : 1
Time         : 0.016s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
CPU Time     : 0.010s

--------------------------------------
predict primecover_highocc.asp: 78%

katinkab@turing:~$ ./Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu4/test_last99.asp 2018-2019/AnswerSetLAD/data/IrvineRepository/HD/mu4/primecover_highocc.asp 2018-2019/AnswerSetLAD/AnswerSetLAD_predict.asp 
clingo version 4.5.4
Reading from ...rvineRepository/HD/mu4/test_last99.asp ...

Solving...
Answer: 1
correctpos(29,of(47)) correctneg(49,of(53)) falsepos(4,of(53)) falseneg(18,of(47))
SATISFIABLE

Models       : 1     
Calls        : 1
Time         : 0.026s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
CPU Time     : 0.020s



