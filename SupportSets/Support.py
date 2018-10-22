# -*- coding: utf-8 -*-

import sys
import pandas
import csv
import numpy as np

"""
This script can be used to calculate a support set from a binary data set consisting of level & interval variables. 
We use the greedy algorithm from Hammer et al. "An implementation of LAD".
"""

def support(binCSV,
	     smallerCSV):
	"""
	User input explained:

	binCSV = CSV input file (for example calculated with BinarizeData.py)
		- the rows are different observations		
		- first column = class of observation
		- following columns = level & interval variables

	smallerCSV = data file name for smaller binary output file consisting of support set
	"""

	print "--- binarize"
        print " input file:", binCSV

	
	#read csv data file
	data = pandas.read_csv(binCSV, header=0, delimiter=",")	
	nbrofrows = len(data)	
	nbrofcol = len(list(data))
	print "  number of rows:", nbrofrows
	print "  number of columns:", nbrofcol
	
	#calculate support set
	
	#first calculate constraint matrix from given binary input file
	#for each pair of true & false point calculate difference vector
	#therefore combine each row of class 1 (class 0) with each row of class 0 (class 1) with higher index 


	diffvect = []
	for ind in range(0,nbrofrows):
		print "this is the class:", data['classes'][ind] 
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
					print diffvect
		
		


if __name__ == '__main__':
      support(*sys.argv[1:])
