# AnswerSetLAD
AnswerSetLAD is a toolbox for pattern generation according to the Logical Analysis of Data making use of Answer Set Programming. 

## Example
#### input data
A input data file is a 0-1 matrix. Each row of the matrix represents an observation. The first column stands for the sign of the observation. The following columns represent the different features which were observed.
An example is given in [10x10input.txt](./data/10x10input.txt):
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
