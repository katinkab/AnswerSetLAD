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

def support(suppCSV):
	"""
	User input explained:

	supCSV = CSV input file (for example calculated with Support.py)
		- the rows are pairs of pos and neg observations	
		- columns are the difference of the pairs in the binary variables
	"""

	print "--- feature selection"
        print " input file:", suppCSV
	
	#read csv data file
	data = pandas.read_csv(suppCSV, header=0, delimiter=",")	
	nbrofrows = len(data)	
	nbrofcol = len(list(data))
	print "  number of rows:", nbrofrows
	print "  number of columns:", nbrofcol
	
	#filename
	originalname = os.path.splitext(suppCSV)[0]
	name = re.sub('\_suppcalc$', '', originalname)
	name = re.sub("2018-2019/AnswerSetLAD/data/IrvineRepository/BreastCancerWis/","",name)

	print "name: ", name

	
	#select features
	#input

	#objective function coefficients u_i (we use the variance of the attribute)
	u = []
	#wir fügen für jede column die varianz/stdabweichung in den vektor u ein
	for ind in range(1,nbrofcol):
		u.append(data.iloc[:,ind].std())

	#constraint coefficients c_ij (we use minimum(dist(cutpoint,p),dist(cutpoint,p'))/spread attribute)	
	#hier brauchen wir original data set!
	c = []

	#right hand side coefficients (how different should the positive and negative be?) 
	#1 \leq mu \leq HamDist(Omega^+, Omega^-)
	#hier erstmal mit mu=1
	mu = []
	for ind in range(1,nbrofrows):
		mu.append(1)

	#initialize
	y = []
	for ind in range(1,nbrofcol):
		y.append(0)

	s = []
	for ind in range(1,nbrofrows):
		s.append(0)

	#start loop
	#def f(i): return 1/u[i]* sum()

	while s < mu :
		#def f(x): return -2 * x**2 + 4 * x
		#max_x = scipy.optimize.fmin(lambda x: -f(x), 0)		



if __name__ == '__main__':
      support(*sys.argv[1:])
