# -*- coding: utf-8 -*-

import sys

#this parser reads from a file including all patterns of a certain type of all degree 
#(starting from degree 1 to any degree (both positive and negative patterns)) (from allpatterns.py for example)
#to generate a file which is usable as input for cover calculation (such as _primecover.asp)

def patternoutput_to_coverinput(FnameIN,
	      FnameOUT):
	"""
	User input explained:

 	FnameIN = TXT file consisting of all patterns as input for cover (calculated with allpatterns.py for example)
	FnameOUT = file name for output
	"""

        print "--- patternoutput_to_coverinput"
        print " input file:", FnameIN

	txt_file  = open(FnameIN, "r") 

	out_file= [""]
    	out_file+= ["%% Data usable for cover calculations from all patterns file %s"%FnameIN]
	out_file+= [""]
	
	patnbr = 0
	#delimiter=","
	sign = 1
	degree = 1

	for line in txt_file:
		if "negative" in line:
			sign = 0
			degree = 1
		if "pat(" in line:
			patnbr = patnbr+1
			mylist = line.split(" ")
			for word in mylist:
				if word.startswith("pat"):
					subword = word[4:].split(",")
					myvariable = subword[0]
					myvalue = subword[-1].split(")")[0]
					out_file+=["pat(%s,%s,%s,(%s,%s))."%(patnbr, sign, degree, myvariable, myvalue)]
				elif word.startswith("covered"):
					subword = word[8:].split(",")
					myobssign = subword[0]
					myobs = subword[-1].split(")")[0]
					out_file+=["cov(%s,%s,%s,(%s,%s))."%(patnbr,sign,degree,myobssign,myobs)]
		if "degree" in line:
			degree = degree+1
			patnbr = 0

	if FnameOUT==None:
        	return "\n".join(out_file)
    	else:
       		with open(FnameOUT, 'w') as f:
           		f.writelines("\n".join(out_file))

	print " output file:", FnameOUT
        print "---"

if __name__ == '__main__':
    patternoutput_to_coverinput(*sys.argv[1:])

