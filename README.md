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
A data file that can be read by the ASP program is created by a call of the function `MakeDataFile.txt2aslad(FnameTXT, FnameASLAD)`. 
To create a readable input data file from the example given above call
`MakeDataFile.txt2aslad("2018/AnswerSetLAD/data/10x10input.txt", "2018/AnswerSetLAD/data/10x10input.aslad")`
