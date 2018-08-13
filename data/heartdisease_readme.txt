7. Attribute Information:
   -- Only 14 used
      -- 1. #3  (age)       
      binary 2. #4  (sex)   (1 = male; 0 = female)     
      nom 3. #9  (cp)       chest pain (1,2,3,4; not ordered) 
      -- 4. #10 (trestbps)  resting blood pressure
      -- 5. #12 (chol)      serum cholestoral
      binary 6. #16 (fbs)   fasting blood sugar
      nom 7. #19 (restecg)  resting electrocardiographic results (0 normal,1,2; not ordered) 
      -- 8. #32 (thalach)   maximum heart rate achieved
      binary 9. #38 (exang) exercise induced angina
      -- 10. #40 (oldpeak)  ST depression induced by exercise relative to rest
      nom 11. #41 (slope)   the slope of the peak exercise ST segment (1 up,2 flat,3 down; not ordered)
      -- 12. #44 (ca)       number of major vessels (0-3) colored by flourosopy
      nom 13. #51 (thal)    3 = normal; 6 = fixed defect; 7 = reversable defect (not ordered)
     _____________________
      -- 14. #58 (num)      diagnosis of heart disease (angiographic disease status)


-> _binary.txt

removed all observations with missing values (?) -> 6 observations removed

classes (common treatment): 
presence (1,2,3,4) -> 1
absence (0) -> 0

nominal attributes:
(cp):
introduce four new binary values:
1 : yes=1, no=0
2 : yes=1, no=0
3 : yes=1, no=0
4 : yes=1, no=0

(restecg):
introduce three new binary values:
0 : yes=1, no=0
1 : yes=1, no=0
2 : yes=1, no=0

(slope):
introduce three new binary values:
1 : yes=1, no=0
2 : yes=1, no=0
3 : yes=1, no=0

(thal):
introduce three new binary values:
3 : yes=1, no=0
6 : yes=1, no=0
7 : yes=1, no=0
