README Credit card scoring

15 attributes
653 observations

Vorgehen:

- delete all observation with missing attributes: 37 -> 653 observations (296 positive, 357 negative)
- moved classes to first column
_________________________________

_suppcalc.csv: 105672 x 773 (etwa 12 stunden rechenzeit)

________________________________

-col1:
a:1
b:2
-col2:
ok
-col3:
ok
-col4:
u:4
y:3
l:2
t:1
-col5:
g:1
p:2
gg:3
-col6:
c:1 
d:2 
cc:3 
i:4
j:5 
k:6 
m:7 
r:8 
q:9 
w:10
x:11 
e:12 
aa:13 
ff:14
-col7:
v:2 
h:3 
bb:4 
j:5 
n:6 
z:7 
dd:8 
ff:9 
o:10
-col8:
ok
-col9:
t:1
f:0
-col10:
t:1
f:0
-col11:
ok
-col12:
t:1
f:0
-col13:
g:1
p:2
s:3
-col14:
ok
-col15:
ok
_________________________________________
From Webpage:

1. Title: Credit Approval

2. Sources: 
    (confidential)
    Submitted by quinlan@cs.su.oz.au

3.  Past Usage:

    See Quinlan,
    * "Simplifying decision trees", Int J Man-Machine Studies 27,
      Dec 1987, pp. 221-234.
    * "C4.5: Programs for Machine Learning", Morgan Kaufmann, Oct 1992
  
4.  Relevant Information:

    This file concerns credit card applications.  All attribute names
    and values have been changed to meaningless symbols to protect
    confidentiality of the data.
  
    This dataset is interesting because there is a good mix of
    attributes -- continuous, nominal with small numbers of
    values, and nominal with larger numbers of values.  There
    are also a few missing values.
  
5.  Number of Instances: 690

6.  Number of Attributes: 15 + class attribute

7.  Attribute Information:

    A1:	b, a.
    A2:	continuous.
    A3:	continuous.
    A4:	u, y, l, t.
    A5:	g, p, gg.
    A6:	c, d, cc, i, j, k, m, r, q, w, x, e, aa, ff.
    A7:	v, h, bb, j, n, z, dd, ff, o.
    A8:	continuous.
    A9:	t, f.
    A10:	t, f.
    A11:	continuous.
    A12:	t, f.
    A13:	g, p, s.
    A14:	continuous.
    A15:	continuous.
    A16: +,-         (class attribute)

8.  Missing Attribute Values:
    37 cases (5%) have one or more missing values.  The missing
    values from particular attributes are:

    A1:  12
    A2:  12
    A4:   6
    A5:   6
    A6:   9
    A7:   9
    A14: 13

9.  Class Distribution
  
    +: 307 (44.5%)
    -: 383 (55.5%)

________________________________
