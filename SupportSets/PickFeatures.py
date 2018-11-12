# -*- coding: utf-8 -*-

import sys
import pandas
import csv
import numpy as np
import os
import re

"""
This script can be used to write a final binary file from "*_fullbinary.csv" data given a calculated support set "support.asp"
"""

def pickfeat(binCSV,
	     support):
	"""
	User input explained:

	binCSV = CSV input file (for example calculated with BinarizeData.py)
		- the rows are different observations		
		- first column = class of observation
		- following columns = level & interval variables

	support = asp data file containing the calculated (with Support.py) support set (e.g. support(5). support(48).)
	"""

	print "--- write small binary file"
        print " from input file:", binCSV
	print " and support set:", support
	
	#read csv data file
	data = pandas.read_csv(binCSV, header=0, delimiter=",")	
	myheader = list(data)
	nbrofrows = len(data)	
	nbrofcol = len(list(data))
	print "  number of rows:", nbrofrows
	print "  number of columns:", nbrofcol
	
	#filename
	originalname = os.path.splitext(binCSV)[0]
	name = re.sub('\_fullbinary$', '', originalname)
	name = re.sub("data/IrvineRepository/BreastCancerWis/","",name)

	print "name: ", name

	#support.asp file
	with open(support, 'r') as myfile:
        	support_string = myfile.read().replace('\n', '')

	columnlist = []

	for word in support_string.split():
		columnlist.append(int(filter(str.isdigit, word)))

	print columnlist

	#new data frame
	shortdata = pandas.DataFrame(data.iloc[:,0])

	for col in columnlist:
		shortdata = pandas.concat([shortdata, data.iloc[:,col]], axis=1)

	print shortdata

	#write data frame to csv
	shortdata.to_csv("2018/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/breastcancerwis_short.csv", index=False)

if __name__ == '__main__':
      pickfeat(*sys.argv[1:])
