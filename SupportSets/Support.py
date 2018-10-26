# -*- coding: utf-8 -*-

import sys
import pandas
import csv
import numpy as np
import os
import re

"""
This script can be used to calculate a support set from a binary data set consisting of level & interval variables. 
We use the greedy algorithm from Hammer et al. "An implementation of LAD".
"""

def support(binCSV,
	     suppCSV):
	"""
	User input explained:

	binCSV = CSV input file (for example calculated with BinarizeData.py)
		- the rows are different observations		
		- first column = class of observation
		- following columns = level & interval variables

	suppCSV = data file name for output file consisting of data frame needed for support set calculation
	"""

	print "--- binarize"
        print " input file:", binCSV
	
	#read csv data file
	data = pandas.read_csv(binCSV, header=0, delimiter=",")	
	nbrofrows = len(data)	
	nbrofcol = len(list(data))
	print "  number of rows:", nbrofrows
	print "  number of columns:", nbrofcol
	
	#filename
	originalname = os.path.splitext(binCSV)[0]
	name = re.sub('\_binary$', '', originalname)
	name = re.sub("data/","",name)

	#dataframe for output
	myheader = list(data)
	suppdata = pandas.DataFrame()
	
	#calculate support set
	
	#first calculate constraint matrix from given binary input file
	#for each pair of true & false point calculate difference vector
	#therefore combine each row of class 1 (class 0) with each row of class 0 (class 1) with higher index 

	diffvect = []
	for ind in range(0,nbrofrows):
		#positive class
		if data['classes'][ind] == 1:
			#we consider all rows with higher indices
			for higherind in range(ind+1,nbrofrows):
				#all observations of opposite class
				diffvect = []
				if data['classes'][higherind] == 0:
					#calculate difference vector
					diffvect = data.iloc[[ind]]
					diffvect = diffvect.append(data.iloc[higherind])
					diffvect = diffvect.sum(axis=0)
					supp = []
					#replace classes by names of rows that are in focus
					supp.append((ind, higherind))
					for entry in diffvect[1:]:
						#no difference = 0 and 2
						#different = 1
						if entry == 2:
							supp.append(0)
						else:
							supp.append(entry)
					df2 = pandas.DataFrame([supp], columns = myheader)
					suppdata = suppdata.append(df2, ignore_index=True)

	suppdata = suppdata.rename(columns={ suppdata.columns[0]: "rows" })	
	print suppdata
	nbrsupprows = len(suppdata)
	nbrsuppcols = len(list(suppdata))
	print "  suppdata number of rows:", nbrsupprows
	print "  suppdata number of cols:", nbrsuppcols

	suppdata.to_csv(suppCSV, index=False)

	#write .asp file for support set calculation
	aspfile = open("data/SupportCalculation/"+name+"_suppcalc.asp","w+") 
	myint = 0
	for ourcol in list(suppdata)[1:]:
		print suppdata[ourcol]
		for ourrow in range(0,nbrsupprows):
			#entry(Zeile, Spalte, Entry)
			print "entry(", ourrow, "," , myint ,"," , suppdata[ourcol][ourrow] , ")."
			aspfile.write("entry("+str(ourrow)+","+str(myint)+","+str(suppdata[ourcol][ourrow])+").\n")
		myint = myint+1
	aspfile.close()
		


if __name__ == '__main__':
      support(*sys.argv[1:])
