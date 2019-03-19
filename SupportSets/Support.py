# -*- coding: utf-8 -*-

import sys
import pandas
import csv
import numpy as np
import os
import re

"""
This script can be used to calculate a matrix of pairwise difference vectors from a binary data set consisting of level & interval variables. 
In a next step we can calculate a support set from it.
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

	print "--- calculate support matrix"
        print " input file:", binCSV
	
	#read csv data file
	data = pandas.read_csv(binCSV, header=0, delimiter=",")	
	nbrofrows = len(data)	
	nbrofcol = len(list(data))-1
	print "  number of rows:", nbrofrows
	print "  number of columns:", nbrofcol
	
	#filename
	#originalname = os.path.splitext(binCSV)[0]
	#name = re.sub('\_disjoint_binary_nointerval$', '', originalname)
	#name = re.sub("2018-2019/AnswerSetLAD/data/IrvineRepository/HeartDisease/disjoint_nointerval/","",name)

	#print "name: ", name

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
			#we consider all rows of opposite sign
			for newind in range(0,nbrofrows):
				#all observations of opposite class
				diffvect = []
				if data['classes'][newind] == 0:
					#calculate difference vector
					diffvect = data.iloc[[ind]]
					diffvect = diffvect.append(data.iloc[newind])
					diffvect = diffvect.sum(axis=0)
					supp = []
					#replace classes by names of rows that are in focus
					supp.append((ind, newind))
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
	nbrsupprows = len(suppdata)
	nbrsuppcols = len(list(suppdata))-1
	print "  suppdata number of rows:", nbrsupprows
	print "  suppdata number of cols:", nbrsuppcols

	suppdata.to_csv(suppCSV, index=False)

	#write .asp file for support set calculation
	#aspfile = open("2018-2019/AnswerSetLAD/data/IrvineRepository/testMarch19/"+name+"_suppcalc.asp","w+") 
	#myint = 0
	#for ourcol in list(suppdata)[1:]:
	#	for ourrow in range(0,nbrsupprows):
			#entry(Zeile, Spalte, Entry)
	#		aspfile.write("entry("+str(ourrow)+","+str(myint)+","+str(suppdata[ourcol][ourrow])+").\n")
	#	myint = myint+1
	#aspfile.close()
		


if __name__ == '__main__':
      support(*sys.argv[1:])
