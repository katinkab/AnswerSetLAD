\ This file was automatically generated by Zimpl
\ param n    := 11;
\ param m    := 73;
\ set I    := { 1 .. m };
\ set J    := { 1 .. n };
\ set K    := { n+1 .. 2*n };
\ set Classes   := {<1,0>, <2,1>, <3,1>, <4,1>, <5,0>, <6,1>, <7,1>, <8,0>, <9,0>, <10,0>, <11,0>, <12,1>, <13,0>, <14,0>, <15,
\ 1>, <16,0>, <17,1>, <18,0>, <19,0>, <20,0>, <21,0>, <22,0>, <23,0>, <24,1>, <25,0>, <26,0>, <27,1>, <28,1>, <29,1>, <30,1>, <
\ 31,1>, <32,1>, <33,0>, <34,1>, <35,1>, <36,1>, <37,1>, <38,1>, <39,0>, <40,1>, <41,0>, <42,1>, <43,1>, <44,1>, <45,0>, <46,0>
\ , <47,0>, <48,0>, <49,1>, <50,0>, <51,0>, <52,0>, <53,1>, <54,1>, <55,1>, <56,1>, <57,0>, <58,0>, <59,1>, <60,1>, <61,1>, <62
\ ,1>, <63,1>, <64,0>, <65,1>, <66,0>, <67,1>, <68,1>, <69,1>, <70,1>, <71,1>, <72,1>, <73,1>};
\ do print Classes;
\ set Positive   := { <k,l> in Classes with l == 1 };
\ do print Positive;
\ set Negative   := { <k,l> in Classes with l == 0 };
\ do print Negative;
\ param a[I*J]  :=     |1,2,3,4,5,6,7,8,9,10,11| |1|1,1,0,1,0,0,1,1,1,0,0| |2|0,1,1,0,1,1,1,1,1,0,1| |3|0,1,1,0,0,1,1,1,1,0,1| 
\ |4|0,0,0,1,0,1,1,1,1,0,1| |5|0,0,1,0,0,1,0,0,0,0,0| |6|1,1,1,1,0,1,1,1,1,0,0| |7|1,1,1,0,0,1,1,1,1,0,0| |8|1,1,0,0,0,1,0,0,0,
\ 0,0| |9|0,0,0,0,0,1,0,0,0,0,0| |10|0,1,1,0,0,0,1,1,1,0,0| |11|1,0,0,0,0,0,0,1,1,0,0| |12|0,1,0,0,0,1,0,1,1,0,1| |13|0,0,0,1,0
\ ,0,1,0,0,0,0| |14|0,0,0,0,0,0,0,0,0,0,1| |15|1,1,1,0,0,1,0,0,0,0,1| |16|1,1,1,0,0,1,1,0,0,0,0| |17|0,0,0,0,1,1,1,1,1,0,1| |18
\ |0,1,1,0,0,0,0,0,0,0,0| |19|0,0,0,0,0,1,0,0,0,0,1| |20|1,0,0,0,0,1,0,1,1,0,0| |21|1,1,0,1,0,1,1,1,1,0,0| |22|0,1,0,1,0,1,1,1,
\ 1,0,0| |23|0,1,1,0,0,0,0,1,1,0,0| |24|0,0,1,0,0,1,1,0,0,0,0| |25|0,0,1,1,0,1,1,1,1,0,0| |26|1,0,0,0,0,1,0,0,0,0,0| |27|0,1,1,
\ 1,0,1,1,1,1,0,0| |28|1,1,0,0,0,1,1,0,0,0,1| |29|0,1,1,0,0,1,1,0,0,0,1| |30|0,0,0,1,1,1,1,1,1,1,1| |31|0,0,0,0,0,1,1,1,1,0,1| 
\ |32|1,0,1,0,0,1,1,1,1,0,0| |33|1,1,0,0,0,1,0,1,1,0,0| |34|1,1,1,0,1,1,0,1,1,0,1| |35|1,1,1,0,0,1,0,1,1,0,1| |36|0,1,1,1,0,1,1
\ ,0,0,1,0| |37|1,0,1,1,0,1,1,1,1,0,1| |38|0,1,1,1,0,1,1,0,0,0,0| |39|1,1,0,0,0,1,1,1,1,0,0| |40|1,1,0,0,1,1,1,1,1,0,1| |41|1,1
\ ,0,0,0,0,1,0,0,0,0| |42|0,1,0,0,1,1,1,1,1,0,1| |43|0,1,0,0,0,1,1,1,1,0,1| |44|0,1,1,0,1,1,0,1,1,0,1| |45|1,1,0,0,0,1,0,0,0,0,
\ 1| |46|1,0,1,0,0,1,0,1,1,0,0| |47|1,1,0,0,1,1,0,0,0,0,1| |48|1,1,0,0,1,1,0,1,1,0,1| |49|0,0,1,0,0,1,1,1,1,0,1| |50|0,1,0,0,0,
\ 0,0,1,1,0,1| |51|0,1,0,1,0,0,1,1,1,0,0| |52|1,1,0,1,0,1,1,0,0,0,0| |53|0,1,1,0,1,1,1,0,0,0,1| |54|1,0,0,0,1,1,1,0,0,0,1| |55|
\ 0,1,1,0,0,0,1,0,0,0,0| |56|1,0,1,0,0,1,1,0,0,0,1| |57|0,0,0,0,0,1,1,0,0,0,1| |58|0,0,1,0,0,1,0,1,1,0,0| |59|0,0,1,0,0,1,1,0,0
\ ,0,1| |60|0,0,1,0,0,1,1,1,0,0,0| |61|0,1,0,0,1,1,0,1,1,0,1| |62|0,1,0,0,0,0,1,0,0,0,1| |63|0,1,0,0,0,1,0,0,0,0,1| |64|0,0,0,0
\ ,0,1,1,1,0,0,0| |65|1,0,0,0,0,1,0,1,1,0,1| |66|0,0,0,0,0,0,0,0,0,0,0| |67|1,1,0,0,0,1,1,0,0,0,0| |68|0,1,0,0,0,0,0,0,0,0,1| |
\ 69|0,1,0,1,1,1,1,1,0,1,1| |70|1,0,1,0,0,1,1,1,1,0,1| |71|0,1,1,0,0,1,0,1,1,0,1| |72|1,1,0,0,0,1,1,1,1,0,1| |73|0,1,0,0,0,0,1,
\ 0,0,0,0|;
\ param aneg[I*K]  :=     |12,13,14,15,16,17,18,19,20,21,22| |1|0,0,1,0,1,1,0,0,0,1,1| |2|1,0,0,1,0,0,0,0,0,1,0| |3|1,0,0,1,1,0
\ ,0,0,0,1,0| |4|1,1,1,0,1,0,0,0,0,1,0| |5|1,1,0,1,1,0,1,1,1,1,1| |6|0,0,0,0,1,0,0,0,0,1,1| |7|0,0,0,1,1,0,0,0,0,1,1| |8|0,0,1,
\ 1,1,0,1,1,1,1,1| |9|1,1,1,1,1,0,1,1,1,1,1| |10|1,0,0,1,1,1,0,0,0,1,1| |11|0,1,1,1,1,1,1,0,0,1,1| |12|1,0,1,1,1,0,1,0,0,1,0| |
\ 13|1,1,1,0,1,1,0,1,1,1,1| |14|1,1,1,1,1,1,1,1,1,1,0| |15|0,0,0,1,1,0,1,1,1,1,0| |16|0,0,0,1,1,0,0,1,1,1,1| |17|1,1,1,1,0,0,0,
\ 0,0,1,0| |18|1,0,0,1,1,1,1,1,1,1,1| |19|1,1,1,1,1,0,1,1,1,1,0| |20|0,1,1,1,1,0,1,0,0,1,1| |21|0,0,1,0,1,0,0,0,0,1,1| |22|1,0,
\ 1,0,1,0,0,0,0,1,1| |23|1,0,0,1,1,1,1,0,0,1,1| |24|1,1,0,1,1,0,0,1,1,1,1| |25|1,1,0,0,1,0,0,0,0,1,1| |26|0,1,1,1,1,0,1,1,1,1,1
\ | |27|1,0,0,0,1,0,0,0,0,1,1| |28|0,0,1,1,1,0,0,1,1,1,0| |29|1,0,0,1,1,0,0,1,1,1,0| |30|1,1,1,0,0,0,0,0,0,0,0| |31|1,1,1,1,1,0
\ ,0,0,0,1,0| |32|0,1,0,1,1,0,0,0,0,1,1| |33|0,0,1,1,1,0,1,0,0,1,1| |34|0,0,0,1,0,0,1,0,0,1,0| |35|0,0,0,1,1,0,1,0,0,1,0| |36|1
\ ,0,0,0,1,0,0,1,1,0,1| |37|0,1,0,0,1,0,0,0,0,1,0| |38|1,0,0,0,1,0,0,1,1,1,1| |39|0,0,1,1,1,0,0,0,0,1,1| |40|0,0,1,1,0,0,0,0,0,
\ 1,0| |41|0,0,1,1,1,1,0,1,1,1,1| |42|1,0,1,1,0,0,0,0,0,1,0| |43|1,0,1,1,1,0,0,0,0,1,0| |44|1,0,0,1,0,0,1,0,0,1,0| |45|0,0,1,1,
\ 1,0,1,1,1,1,0| |46|0,1,0,1,1,0,1,0,0,1,1| |47|0,0,1,1,0,0,1,1,1,1,0| |48|0,0,1,1,0,0,1,0,0,1,0| |49|1,1,0,1,1,0,0,0,0,1,0| |5
\ 0|1,0,1,1,1,1,1,0,0,1,0| |51|1,0,1,0,1,1,0,0,0,1,1| |52|0,0,1,0,1,0,0,1,1,1,1| |53|1,0,0,1,0,0,0,1,1,1,0| |54|0,1,1,1,0,0,0,1
\ ,1,1,0| |55|1,0,0,1,1,1,0,1,1,1,1| |56|0,1,0,1,1,0,0,1,1,1,0| |57|1,1,1,1,1,0,0,1,1,1,0| |58|1,1,0,1,1,0,1,0,0,1,1| |59|1,1,0
\ ,1,1,0,0,1,1,1,0| |60|1,1,0,1,1,0,0,0,1,1,1| |61|1,0,1,1,0,0,1,0,0,1,0| |62|1,0,1,1,1,1,0,1,1,1,0| |63|1,0,1,1,1,0,1,1,1,1,0|
\  |64|1,1,1,1,1,0,0,0,1,1,1| |65|0,1,1,1,1,0,1,0,0,1,0| |66|1,1,1,1,1,1,1,1,1,1,1| |67|0,0,1,1,1,0,0,1,1,1,1| |68|1,0,1,1,1,1,
\ 1,1,1,1,0| |69|1,0,1,0,0,0,0,0,1,0,0| |70|0,1,0,1,1,0,0,0,0,1,0| |71|1,0,0,1,1,0,1,0,0,1,0| |72|0,0,1,1,1,0,0,0,0,1,0| |73|1,
\ 0,1,1,1,1,0,1,1,1,1|;
\ var Y[Positive] binary;
\ var X[J] binary;
\ var Xneg[K] binary;
\ var degree integer >= 1 <= n ;
\ minimize notcovered: sum <k,l> in Positive: Y[k,l];
\ subto onlyone:  forall <j> in J do   X[j] + Xneg[j+n] <= 1 ;
\ subto patterndegree: sum <j> in J : X[j] + sum <k> in K : Xneg[k] == degree;
\ subto opposallnotcovered:  forall <i,l> in Negative do     sum <j> in J : (a[i,j] * X[j]) + sum <k> in K : (aneg[i,k] * Xneg[
\ k]) <= degree - 1;
\ subto atleastonecovered: forall <i,l> in Positive do     sum <j> in J : a[i,j] * X[j] + n * Y[i,l] + sum <k> in K : aneg[i,k]
\  * Xneg[k] + n * Y[i,l] >= degree;
\Problem name: 2018-2019/MIPsForLAD/strongest_HD_3fold_mu4.zpl
Minimize
 notcovered:  + Y#2#1 + Y#3#1 + Y#4#1 + Y#6#1 + Y#7#1 + Y#12#1
  + Y#15#1 + Y#17#1 + Y#24#1 + Y#27#1 + Y#28#1 + Y#29#1
  + Y#30#1 + Y#31#1 + Y#32#1 + Y#34#1 + Y#35#1 + Y#36#1
  + Y#37#1 + Y#38#1 + Y#40#1 + Y#42#1 + Y#43#1 + Y#44#1
  + Y#49#1 + Y#53#1 + Y#54#1 + Y#55#1 + Y#56#1 + Y#59#1
  + Y#60#1 + Y#61#1 + Y#62#1 + Y#63#1 + Y#65#1 + Y#67#1
  + Y#68#1 + Y#69#1 + Y#70#1 + Y#71#1 + Y#72#1 + Y#73#1
 
Subject to
 objval:
  + Y#2#1 + Y#3#1 + Y#4#1 + Y#6#1 + Y#7#1 + Y#12#1
  + Y#15#1 + Y#17#1 + Y#24#1 + Y#27#1 + Y#28#1 + Y#29#1
  + Y#30#1 + Y#31#1 + Y#32#1 + Y#34#1 + Y#35#1 + Y#36#1
  + Y#37#1 + Y#38#1 + Y#40#1 + Y#42#1 + Y#43#1 + Y#44#1
  + Y#49#1 + Y#53#1 + Y#54#1 + Y#55#1 + Y#56#1 + Y#59#1
  + Y#60#1 + Y#61#1 + Y#62#1 + Y#63#1 + Y#65#1 + Y#67#1
  + Y#68#1 + Y#69#1 + Y#70#1 + Y#71#1 + Y#72#1 + Y#73#1 == 28
 onlyone_1:
  + Xneg#12 + X#1 <= 1
 onlyone_2:
  + Xneg#13 + X#2 <= 1
 onlyone_3:
  + Xneg#14 + X#3 <= 1
 onlyone_4:
  + Xneg#15 + X#4 <= 1
 onlyone_5:
  + Xneg#16 + X#5 <= 1
 onlyone_6:
  + Xneg#17 + X#6 <= 1
 onlyone_7:
  + Xneg#18 + X#7 <= 1
 onlyone_8:
  + Xneg#19 + X#8 <= 1
 onlyone_9:
  + Xneg#20 + X#9 <= 1
 onlyone_10:
  + Xneg#21 + X#10 <= 1
 onlyone_11:
  + Xneg#22 + X#11 <= 1
 patterndegree_1:
  - degree + Xneg#22 + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#18
  + Xneg#17 + Xneg#16 + Xneg#15 + Xneg#14 + Xneg#13 + Xneg#12
  + X#11 + X#10 + X#9 + X#8 + X#7 + X#6
  + X#5 + X#4 + X#3 + X#2 + X#1 = 0
 opposallnotcov@c:
  - degree + Xneg#22 + Xneg#21 + Xneg#17 + Xneg#16 + Xneg#14
  + X#9 + X#8 + X#7 + X#4 + X#2 + X#1
  <= -1
 opposallnotcov@d:
  - degree + Xneg#22 + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#18
  + Xneg#16 + Xneg#15 + Xneg#13 + Xneg#12 + X#6 + X#3
  <= -1
 opposallnotcov@e:
  - degree + Xneg#22 + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#18
  + Xneg#16 + Xneg#15 + Xneg#14 + X#6 + X#2 + X#1
  <= -1
 opposallnotcov@f:
  - degree + Xneg#22 + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#18
  + Xneg#16 + Xneg#15 + Xneg#14 + Xneg#13 + Xneg#12 + X#6
  <= -1
 opposallnotco@10:
  - degree + Xneg#22 + Xneg#21 + Xneg#17 + Xneg#16 + Xneg#15
  + Xneg#12 + X#9 + X#8 + X#7 + X#3 + X#2
  <= -1
 opposallnotco@11:
  - degree + Xneg#22 + Xneg#21 + Xneg#18 + Xneg#17 + Xneg#16
  + Xneg#15 + Xneg#14 + Xneg#13 + X#9 + X#8 + X#1
  <= -1
 opposallnotco@12:
  - degree + Xneg#22 + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#17
  + Xneg#16 + Xneg#14 + Xneg#13 + Xneg#12 + X#7 + X#4
  <= -1
 opposallnotco@13:
  - degree + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#18 + Xneg#17
  + Xneg#16 + Xneg#15 + Xneg#14 + Xneg#13 + Xneg#12 + X#11
  <= -1
 opposallnotco@14:
  - degree + Xneg#22 + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#16
  + Xneg#15 + X#7 + X#6 + X#3 + X#2 + X#1
  <= -1
 opposallnotco@15:
  - degree + Xneg#22 + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#18
  + Xneg#17 + Xneg#16 + Xneg#15 + Xneg#12 + X#3 + X#2
  <= -1
 opposallnotco@16:
  - degree + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#18 + Xneg#16
  + Xneg#15 + Xneg#14 + Xneg#13 + Xneg#12 + X#11 + X#6
  <= -1
 opposallnotco@17:
  - degree + Xneg#22 + Xneg#21 + Xneg#18 + Xneg#16 + Xneg#15
  + Xneg#14 + Xneg#13 + X#9 + X#8 + X#6 + X#1
  <= -1
 opposallnotco@18:
  - degree + Xneg#22 + Xneg#21 + Xneg#16 + Xneg#14 + X#9
  + X#8 + X#7 + X#6 + X#4 + X#2 + X#1
  <= -1
 opposallnotco@19:
  - degree + Xneg#22 + Xneg#21 + Xneg#16 + Xneg#14 + Xneg#12
  + X#9 + X#8 + X#7 + X#6 + X#4 + X#2
  <= -1
 opposallnotco@1a:
  - degree + Xneg#22 + Xneg#21 + Xneg#18 + Xneg#17 + Xneg#16
  + Xneg#15 + Xneg#12 + X#9 + X#8 + X#3 + X#2
  <= -1
 opposallnotco@1b:
  - degree + Xneg#22 + Xneg#21 + Xneg#16 + Xneg#13 + Xneg#12
  + X#9 + X#8 + X#7 + X#6 + X#4 + X#3
  <= -1
 opposallnotco@1c:
  - degree + Xneg#22 + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#18
  + Xneg#16 + Xneg#15 + Xneg#14 + Xneg#13 + X#6 + X#1
  <= -1
 opposallnotco@1d:
  - degree + Xneg#22 + Xneg#21 + Xneg#18 + Xneg#16 + Xneg#15
  + Xneg#14 + X#9 + X#8 + X#6 + X#2 + X#1
  <= -1
 opposallnotco@1e:
  - degree + Xneg#22 + Xneg#21 + Xneg#16 + Xneg#15 + Xneg#14
  + X#9 + X#8 + X#7 + X#6 + X#2 + X#1
  <= -1
 opposallnotco@1f:
  - degree + Xneg#22 + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#17
  + Xneg#16 + Xneg#15 + Xneg#14 + X#7 + X#2 + X#1
  <= -1
 opposallnotco@20:
  - degree + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#18 + Xneg#16
  + Xneg#15 + Xneg#14 + X#11 + X#6 + X#2 + X#1
  <= -1
 opposallnotco@21:
  - degree + Xneg#22 + Xneg#21 + Xneg#18 + Xneg#16 + Xneg#15
  + Xneg#13 + X#9 + X#8 + X#6 + X#3 + X#1
  <= -1
 opposallnotco@22:
  - degree + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#18 + Xneg#15
  + Xneg#14 + X#11 + X#6 + X#5 + X#2 + X#1
  <= -1
 opposallnotco@23:
  - degree + Xneg#21 + Xneg#18 + Xneg#15 + Xneg#14 + X#11
  + X#9 + X#8 + X#6 + X#5 + X#2 + X#1
  <= -1
 opposallnotco@24:
  - degree + Xneg#21 + Xneg#18 + Xneg#17 + Xneg#16 + Xneg#15
  + Xneg#14 + Xneg#12 + X#11 + X#9 + X#8 + X#2
  <= -1
 opposallnotco@25:
  - degree + Xneg#22 + Xneg#21 + Xneg#17 + Xneg#16 + Xneg#14
  + Xneg#12 + X#9 + X#8 + X#7 + X#4 + X#2
  <= -1
 opposallnotco@26:
  - degree + Xneg#22 + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#16
  + Xneg#14 + X#7 + X#6 + X#4 + X#2 + X#1
  <= -1
 opposallnotco@27:
  - degree + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#16 + Xneg#15
  + Xneg#14 + Xneg#13 + Xneg#12 + X#11 + X#7 + X#6
  <= -1
 opposallnotco@28:
  - degree + Xneg#22 + Xneg#21 + Xneg#18 + Xneg#16 + Xneg#15
  + Xneg#13 + Xneg#12 + X#9 + X#8 + X#6 + X#3
  <= -1
 opposallnotco@29:
  - degree + Xneg#22 + Xneg#21 + Xneg#20 + Xneg#16 + Xneg#15
  + Xneg#14 + Xneg#13 + Xneg#12 + X#8 + X#7 + X#6
  <= -1
 opposallnotco@2a:
  - degree + Xneg#22 + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#18
  + Xneg#17 + Xneg#16 + Xneg#15 + Xneg#14 + Xneg#13 + Xneg#12
  <= -1
 atleastonecov@2b:
  - degree + Xneg#21 + Xneg#15 + Xneg#12 +22 Y#2#1 + X#11
  + X#9 + X#8 + X#7 + X#6 + X#5 + X#3
  + X#2 >= 0
 atleastonecov@2c:
  - degree + Xneg#21 + Xneg#16 + Xneg#15 + Xneg#12 +22 Y#3#1
  + X#11 + X#9 + X#8 + X#7 + X#6 + X#3
  + X#2 >= 0
 atleastonecov@2d:
  - degree + Xneg#21 + Xneg#16 + Xneg#14 + Xneg#13 + Xneg#12
  +22 Y#4#1 + X#11 + X#9 + X#8 + X#7 + X#6
  + X#4 >= 0
 atleastonecov@2e:
  - degree + Xneg#22 + Xneg#21 + Xneg#16 +22 Y#6#1 + X#9
  + X#8 + X#7 + X#6 + X#4 + X#3 + X#2
  + X#1 >= 0
 atleastonecov@2f:
  - degree + Xneg#22 + Xneg#21 + Xneg#16 + Xneg#15 +22 Y#7#1
  + X#9 + X#8 + X#7 + X#6 + X#3 + X#2
  + X#1 >= 0
 atleastonecov@30:
  - degree + Xneg#21 + Xneg#18 + Xneg#16 + Xneg#15 + Xneg#14
  + Xneg#12 +22 Y#12#1 + X#11 + X#9 + X#8 + X#6
  + X#2 >= 0
 atleastonecov@31:
  - degree + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#18 + Xneg#16
  + Xneg#15 +22 Y#15#1 + X#11 + X#6 + X#3 + X#2
  + X#1 >= 0
 atleastonecov@32:
  - degree + Xneg#21 + Xneg#15 + Xneg#14 + Xneg#13 + Xneg#12
  +22 Y#17#1 + X#11 + X#9 + X#8 + X#7 + X#6
  + X#5 >= 0
 atleastonecov@33:
  - degree + Xneg#22 + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#16
  + Xneg#15 + Xneg#13 + Xneg#12 +22 Y#24#1 + X#7 + X#6
  + X#3 >= 0
 atleastonecov@34:
  - degree + Xneg#22 + Xneg#21 + Xneg#16 + Xneg#12 +22 Y#27#1
  + X#9 + X#8 + X#7 + X#6 + X#4 + X#3
  + X#2 >= 0
 atleastonecov@35:
  - degree + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#16 + Xneg#15
  + Xneg#14 +22 Y#28#1 + X#11 + X#7 + X#6 + X#2
  + X#1 >= 0
 atleastonecov@36:
  - degree + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#16 + Xneg#15
  + Xneg#12 +22 Y#29#1 + X#11 + X#7 + X#6 + X#3
  + X#2 >= 0
 atleastonecov@37:
  - degree + Xneg#14 + Xneg#13 + Xneg#12 +22 Y#30#1 + X#11
  + X#10 + X#9 + X#8 + X#7 + X#6 + X#5
  + X#4 >= 0
 atleastonecov@38:
  - degree + Xneg#21 + Xneg#16 + Xneg#15 + Xneg#14 + Xneg#13
  + Xneg#12 +22 Y#31#1 + X#11 + X#9 + X#8 + X#7
  + X#6 >= 0
 atleastonecov@39:
  - degree + Xneg#22 + Xneg#21 + Xneg#16 + Xneg#15 + Xneg#13
  +22 Y#32#1 + X#9 + X#8 + X#7 + X#6 + X#3
  + X#1 >= 0
 atleastonecov@3a:
  - degree + Xneg#21 + Xneg#18 + Xneg#15 +22 Y#34#1 + X#11
  + X#9 + X#8 + X#6 + X#5 + X#3 + X#2
  + X#1 >= 0
 atleastonecov@3b:
  - degree + Xneg#21 + Xneg#18 + Xneg#16 + Xneg#15 +22 Y#35#1
  + X#11 + X#9 + X#8 + X#6 + X#3 + X#2
  + X#1 >= 0
 atleastonecov@3c:
  - degree + Xneg#22 + Xneg#20 + Xneg#19 + Xneg#16 + Xneg#12
  +22 Y#36#1 + X#10 + X#7 + X#6 + X#4 + X#3
  + X#2 >= 0
 atleastonecov@3d:
  - degree + Xneg#21 + Xneg#16 + Xneg#13 +22 Y#37#1 + X#11
  + X#9 + X#8 + X#7 + X#6 + X#4 + X#3
  + X#1 >= 0
 atleastonecov@3e:
  - degree + Xneg#22 + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#16
  + Xneg#12 +22 Y#38#1 + X#7 + X#6 + X#4 + X#3
  + X#2 >= 0
 atleastonecov@3f:
  - degree + Xneg#21 + Xneg#15 + Xneg#14 +22 Y#40#1 + X#11
  + X#9 + X#8 + X#7 + X#6 + X#5 + X#2
  + X#1 >= 0
 atleastonecov@40:
  - degree + Xneg#21 + Xneg#15 + Xneg#14 + Xneg#12 +22 Y#42#1
  + X#11 + X#9 + X#8 + X#7 + X#6 + X#5
  + X#2 >= 0
 atleastonecov@41:
  - degree + Xneg#21 + Xneg#16 + Xneg#15 + Xneg#14 + Xneg#12
  +22 Y#43#1 + X#11 + X#9 + X#8 + X#7 + X#6
  + X#2 >= 0
 atleastonecov@42:
  - degree + Xneg#21 + Xneg#18 + Xneg#15 + Xneg#12 +22 Y#44#1
  + X#11 + X#9 + X#8 + X#6 + X#5 + X#3
  + X#2 >= 0
 atleastonecov@43:
  - degree + Xneg#21 + Xneg#16 + Xneg#15 + Xneg#13 + Xneg#12
  +22 Y#49#1 + X#11 + X#9 + X#8 + X#7 + X#6
  + X#3 >= 0
 atleastonecov@44:
  - degree + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#15 + Xneg#12
  +22 Y#53#1 + X#11 + X#7 + X#6 + X#5 + X#3
  + X#2 >= 0
 atleastonecov@45:
  - degree + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#15 + Xneg#14
  + Xneg#13 +22 Y#54#1 + X#11 + X#7 + X#6 + X#5
  + X#1 >= 0
 atleastonecov@46:
  - degree + Xneg#22 + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#17
  + Xneg#16 + Xneg#15 + Xneg#12 +22 Y#55#1 + X#7 + X#3
  + X#2 >= 0
 atleastonecov@47:
  - degree + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#16 + Xneg#15
  + Xneg#13 +22 Y#56#1 + X#11 + X#7 + X#6 + X#3
  + X#1 >= 0
 atleastonecov@48:
  - degree + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#16 + Xneg#15
  + Xneg#13 + Xneg#12 +22 Y#59#1 + X#11 + X#7 + X#6
  + X#3 >= 0
 atleastonecov@49:
  - degree + Xneg#22 + Xneg#21 + Xneg#20 + Xneg#16 + Xneg#15
  + Xneg#13 + Xneg#12 +22 Y#60#1 + X#8 + X#7 + X#6
  + X#3 >= 0
 atleastonecov@4a:
  - degree + Xneg#21 + Xneg#18 + Xneg#15 + Xneg#14 + Xneg#12
  +22 Y#61#1 + X#11 + X#9 + X#8 + X#6 + X#5
  + X#2 >= 0
 atleastonecov@4b:
  - degree + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#17 + Xneg#16
  + Xneg#15 + Xneg#14 + Xneg#12 +22 Y#62#1 + X#11 + X#7
  + X#2 >= 0
 atleastonecov@4c:
  - degree + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#18 + Xneg#16
  + Xneg#15 + Xneg#14 + Xneg#12 +22 Y#63#1 + X#11 + X#6
  + X#2 >= 0
 atleastonecov@4d:
  - degree + Xneg#21 + Xneg#18 + Xneg#16 + Xneg#15 + Xneg#14
  + Xneg#13 +22 Y#65#1 + X#11 + X#9 + X#8 + X#6
  + X#1 >= 0
 atleastonecov@4e:
  - degree + Xneg#22 + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#16
  + Xneg#15 + Xneg#14 +22 Y#67#1 + X#7 + X#6 + X#2
  + X#1 >= 0
 atleastonecov@4f:
  - degree + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#18 + Xneg#17
  + Xneg#16 + Xneg#15 + Xneg#14 + Xneg#12 +22 Y#68#1 + X#11
  + X#2 >= 0
 atleastonecov@50:
  - degree + Xneg#20 + Xneg#14 + Xneg#12 +22 Y#69#1 + X#11
  + X#10 + X#8 + X#7 + X#6 + X#5 + X#4
  + X#2 >= 0
 atleastonecov@51:
  - degree + Xneg#21 + Xneg#16 + Xneg#15 + Xneg#13 +22 Y#70#1
  + X#11 + X#9 + X#8 + X#7 + X#6 + X#3
  + X#1 >= 0
 atleastonecov@52:
  - degree + Xneg#21 + Xneg#18 + Xneg#16 + Xneg#15 + Xneg#12
  +22 Y#71#1 + X#11 + X#9 + X#8 + X#6 + X#3
  + X#2 >= 0
 atleastonecov@53:
  - degree + Xneg#21 + Xneg#16 + Xneg#15 + Xneg#14 +22 Y#72#1
  + X#11 + X#9 + X#8 + X#7 + X#6 + X#2
  + X#1 >= 0
 atleastonecov@54:
  - degree + Xneg#22 + Xneg#21 + Xneg#20 + Xneg#19 + Xneg#17
  + Xneg#16 + Xneg#15 + Xneg#14 + Xneg#12 +22 Y#73#1 + X#7
  + X#2 >= 0
Bounds
 0 <= Y#2#1 <= 1
 0 <= Y#3#1 <= 1
 0 <= Y#4#1 <= 1
 0 <= Y#6#1 <= 1
 0 <= Y#7#1 <= 1
 0 <= Y#12#1 <= 1
 0 <= Y#15#1 <= 1
 0 <= Y#17#1 <= 1
 0 <= Y#24#1 <= 1
 0 <= Y#27#1 <= 1
 0 <= Y#28#1 <= 1
 0 <= Y#29#1 <= 1
 0 <= Y#30#1 <= 1
 0 <= Y#31#1 <= 1
 0 <= Y#32#1 <= 1
 0 <= Y#34#1 <= 1
 0 <= Y#35#1 <= 1
 0 <= Y#36#1 <= 1
 0 <= Y#37#1 <= 1
 0 <= Y#38#1 <= 1
 0 <= Y#40#1 <= 1
 0 <= Y#42#1 <= 1
 0 <= Y#43#1 <= 1
 0 <= Y#44#1 <= 1
 0 <= Y#49#1 <= 1
 0 <= Y#53#1 <= 1
 0 <= Y#54#1 <= 1
 0 <= Y#55#1 <= 1
 0 <= Y#56#1 <= 1
 0 <= Y#59#1 <= 1
 0 <= Y#60#1 <= 1
 0 <= Y#61#1 <= 1
 0 <= Y#62#1 <= 1
 0 <= Y#63#1 <= 1
 0 <= Y#65#1 <= 1
 0 <= Y#67#1 <= 1
 0 <= Y#68#1 <= 1
 0 <= Y#69#1 <= 1
 0 <= Y#70#1 <= 1
 0 <= Y#71#1 <= 1
 0 <= Y#72#1 <= 1
 0 <= Y#73#1 <= 1
 0 <= X#1 <= 1
 0 <= X#2 <= 1
 0 <= X#3 <= 1
 0 <= X#4 <= 1
 0 <= X#5 <= 1
 0 <= X#6 <= 1
 0 <= X#7 <= 1
 0 <= X#8 <= 1
 0 <= X#9 <= 1
 0 <= X#10 <= 1
 0 <= X#11 <= 1
 0 <= Xneg#12 <= 1
 0 <= Xneg#13 <= 1
 0 <= Xneg#14 <= 1
 0 <= Xneg#15 <= 1
 0 <= Xneg#16 <= 1
 0 <= Xneg#17 <= 1
 0 <= Xneg#18 <= 1
 0 <= Xneg#19 <= 1
 0 <= Xneg#20 <= 1
 0 <= Xneg#21 <= 1
 0 <= Xneg#22 <= 1
 1 <= degree <= 11
General
 Y#2#1
 Y#3#1
 Y#4#1
 Y#6#1
 Y#7#1
 Y#12#1
 Y#15#1
 Y#17#1
 Y#24#1
 Y#27#1
 Y#28#1
 Y#29#1
 Y#30#1
 Y#31#1
 Y#32#1
 Y#34#1
 Y#35#1
 Y#36#1
 Y#37#1
 Y#38#1
 Y#40#1
 Y#42#1
 Y#43#1
 Y#44#1
 Y#49#1
 Y#53#1
 Y#54#1
 Y#55#1
 Y#56#1
 Y#59#1
 Y#60#1
 Y#61#1
 Y#62#1
 Y#63#1
 Y#65#1
 Y#67#1
 Y#68#1
 Y#69#1
 Y#70#1
 Y#71#1
 Y#72#1
 Y#73#1
 X#1
 X#2
 X#3
 X#4
 X#5
 X#6
 X#7
 X#8
 X#9
 X#10
 X#11
 Xneg#12
 Xneg#13
 Xneg#14
 Xneg#15
 Xneg#16
 Xneg#17
 Xneg#18
 Xneg#19
 Xneg#20
 Xneg#21
 Xneg#22
 degree
End
