# AnswerSetLAD
AnswerSetLAD is a software package for data binarization, pattern generation and theory formation according to the _Logical Analysis of Data_ (LAD) making use of _Answer Set Programming_ (ASP). 

## Definitions

### Homogeneity of a pattern
The _homogeneity_ _Hom⁺(P)_ of a positive pattern _P_ is given by
```
Hom⁺(P)=|Cov(P)|/|Cov_total(P)|,
```
where _Cov(P)_ is the set of positive observations covered by _P_ and _Cov_total(P)_ is the set of observations covered in total. The homogeneity _Hom⁻(P)_  of a negative pattern _P_ is defined analogously.

### Prevalence of a pattern
The _prevalence_ _Prev⁺(P)_ of a positive pattern _P_ is given by
```
Prev⁺(P)=|Cov(P)|/|Ω⁺|,
```
where _Cov(P)_ is the set of positive observations covered by _P_ and _Ω⁺_ is the set of positive observations. The prevalence _Prev⁻(P)_ of a negative pattern _P_ is defined analogously.

## Example
### Input data
An input data file is a 0-1 matrix. Each row of the matrix represents an observation. The first column stands for the sign of the observation. The following columns represent the different features that were observed.
An example of a suitable input data file is given in [10x10input.txt](./data/10x10input.txt):
```
1,1,0,0,0,0,1,1,1,0,0
1,1,0,0,0,0,1,0,0,0,0
1,0,1,1,0,0,1,0,1,0,0
1,0,1,1,0,0,0,1,1,0,0
1,1,0,1,0,0,1,1,1,0,0
0,0,1,0,1,1,0,0,1,1,0
0,0,0,0,1,0,1,0,1,1,0
0,0,1,0,0,0,1,0,1,0,1
0,0,1,0,0,0,0,0,1,0,1
0,0,0,0,1,1,0,0,1,1,0
```
### Generating a readable input data file
A data file that can be read by the ASP program is created by a call of `MakeDataFile.py`. The script requires two arguments. These are:

 * the direction to the input data file;
 * the direction to the output data file.

For the example given above we call
```
python MakeDataFile.py data/10x10input.txt data/10x10input.asp
```
and create a readable output file. 
The output file consists of facts
```
i(sign, observationnumber, featurenumber, featurevalue).
```
where 
 * _sign_ is the sign of the observation, 
 * _observationnumber_ is the number of the observation,
 * _featurenumber_ is the ID number of the feature,
 * _featurevalue_ is the value of the feature.

The first row of the given example data in [10x10input.txt](./data/10x10input.txt) therefore looks like this in the output file:
```
i(1,1,1,1).
i(1,1,2,0).
i(1,1,3,0).
i(1,1,4,0).
i(1,1,5,0).
i(1,1,6,1).
i(1,1,7,1).
i(1,1,8,1).
i(1,1,9,0).
i(1,1,10,0).
```

### Pattern generation

To execute the files for pattern generation we use the ASP solver _clingo_ by [Potassco](https://potassco.org/). 
Various types of patterns are implemented, namely:
 * general patterns [AnswerSetLAD_pattern.asp](./AnswerSetLAD_pattern.asp)
 * prime patterns [AnswerSetLAD_prime.asp](./AnswerSetLAD_prime.asp) 
 * strong patterns [AnswerSetLAD_strong.asp](./AnswerSetLAD_strong.asp)
 * spanned patterns [AnswerSetLAD_spanned.asp](./AnswerSetLAD_spanned.asp)
 * strong prime patterns [AnswerSetLAD_strongprime.asp](./AnswerSetLAD_strongprime.asp)
 * strong spanned patterns [AnswerSetLAD_strongspanned.asp](./AnswerSetLAD_strongspanned.asp)
 * maximal patterns [AnswerSetLAD_maximal.asp](./AnswerSetLAD_maximal.asp)
 
Each of the pattern generation files include up to four constants that have to be specified by the user (otherwise they are set to the default option). These constants are

 * _sign_ is the sign of the pattern;
 * _degree_ is the degree of the pattern;
 * _homogeneity_ is the homogeneity of the pattern given as a percentage;
 * _prevalence_ is the prevalence of the pattern given as a percentage;

see the definitions above for explanation.

To calculate a positive prime pattern of degree two from the toy data set call:
 
```
$ clingo data/10x10input.asp AnswerSetLAD_prime.asp -c sign=1 -c degree=2 -c homogeneity=100 -c prevalence=0 
```
The problem will be solved and the terminal displays the following answer:
```
Solving...
Answer: 1
pat(9,0) pat(10,0)
SATISFIABLE
```
The answer set is a set of literals _pat(featurenumber,featurevalue)_ which are combined by AND gates. This answer set represents the prime pattern `NOT feature 9 AND NOT feature 10`.

The answer set of each program is one pattern fulfilling the given constraints. To see all optimal patterns use the `-n 0` option of _clingo_:
```
$ clingo data/10x10input.asp AnswerSetLAD_prime.asp -c sign=1 -c degree=2 -c homogeneity=100 -c prevalence=0 -n 0

Solving...
Answer: 1
pat(9,0) pat(10,0)
Answer: 2
pat(4,0) pat(10,0)
Answer: 3
pat(2,0) pat(4,0)
Answer: 4
pat(2,0) pat(9,0)
SATISFIABLE
```
This result shows all positive prime patterns of degree two with perfect homogeneity and trivial bound on the prevalence.

#### Pattern generation using _asprin_
For the calculation of Pareto-optimal patterns we implemented the option to solve the problem instances using _asprin_ (https://github.com/potassco/asprin), which is a general framework for optimization in ASP. 

#### Calculating all patterns for a data set

To calculate all positive and negative patterns between a lower bound on the degree and an upper bound on the degree use the script `allpatterns.py`. It requires six (up to seven) arguments. These are:

 * the input data file;
 * the file that should be used for pattern calculation;
 * the lower bound on the degree;
 * the upper bound on the degree;
 * the lower bound on the homogeneity;
 * the lower bound on the prevalence;
 * "quiet" if you do not want all patterns to be listed (optional).

The function call

```
python allpatterns.py data/10x10input.asp AnswerSetLAD_strong.asp 1 10 90 10

```
will thus calculate all strong patterns in the example data set from degree 1 to degree 10 with homogeneity greater or equal 90 percent and prevalence greater or equal 10 percent.


## Additional folders
 * [ASPvsMIP](./ASPvsMIP) contains data files and MILP for the comparison between ASP and MIP with regards to maximal pattern generation.
 * [DataBinarization](./DataBinarization) includes a _python_ program for the binarization of a numerical data set based on the introduction of level (and interval) variables.
 * [PerformanceTesting](./PerformanceTesting) contains programs for k-fold crossvalidation tests.
 * [SupportSets](./SupportSets) is part of the binarization step. It includes programs for support set calculation and greedy feature selection.
 * [TheoryFormation](./TheoryFormation) includes programs to calculate pattern covers and make predictions;
 * [data](./data) contains example data files both in .txt as well as in the required .asp format.

