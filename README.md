# AnswerSetLAD
AnswerSetLAD is a toolbox for pattern generation according to the Logical Analysis of Data (LAD) making use of Answer Set Programming (ASP). 

## Example
#### Input data
An input data file is a 0-1 matrix. Each row of the matrix represents an observation. The first column stands for the sign of the observation. The following columns represent the different features which were observed.
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
#### Generating a readable input data file
A data file that can be read by the ASP program is created by a call of the function `MakeDataFile.txt2asp(FnameTXT, FnameASP)`.
For the example given above we call
```
MakeDataFile.txt2asp("data/10x10input.txt", "data/10x10input.asp")
```
and create a readable output file. 
The output file consists of facts
```
i(sign, observationnumber, featurenumber, featurevalue).
```
where 
 * 'sign' is the sign of the observation, 
 * 'observationnumber' is the number of the observation,
 * 'featurenumber' is the number of the feature,
 * 'featurevalue' is the value of the feature.

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
