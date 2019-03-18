# -*- coding: utf-8 -*-

import sys
import pandas
import csv
import numpy as np
import os
import re

"""
This script can be used to write a final binary file from "*_binary.csv" data given a calculated support set via Greedy.py
"""

def pickfeatgreedy(binCSV,
	     support, OutFile):
	"""
	User input explained:

	binCSV = CSV input file (for example calculated with BinarizeData.py)
		- the rows are different observations		
		- first column = class of observation
		- following columns = level & interval variables

	support = calculated support set via Greedy.py (including column numbers to keep)
	"""

	print "--- write small binary file"
        print " from input file:", binCSV
	print " and support set:", support
	
	#read csv data file
	data = pandas.read_csv(binCSV, header=0, delimiter=",")	
	myheader = list(data)
	nbrofrows = len(data)	
	nbrofcol = len(list(data))-1
	print "  number of rows:", nbrofrows
	print "  number of columns:", nbrofcol

	columnlist = []

	#file including number of columns to keep
	with open(support, 'r') as myfile:
        	for line in myfile:
			#if line not empty
			if line.strip():
				if not "%" in line:
					mycol = "".join(i for i in line if i.isdigit())
					columnlist.append(int(mycol))
	#print columnlist

	#new data frame
	shortdata = pandas.DataFrame(data.iloc[:,0])

	for col in columnlist:
		shortdata = pandas.concat([shortdata, data.iloc[:,col+1]], axis=1)

	#write data frame to csv
	shortdata.to_csv(OutFile, index=False)

if __name__ == '__main__':
      pickfeatgreedy(*sys.argv[1:])
