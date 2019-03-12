# -*- coding: utf-8 -*-

import sys
import pandas
import csv
import numpy as np
import os
import re
import random

"""
This script can be used to calculate a support set from a binary data set consisting of level & interval variables. 
We use the greedy algorithm from Hammer et al. "An implementation of LAD".
"""

def support(suppCSV,classesCSV):
	"""
	User input explained:

	supCSV = CSV input file (for example calculated with Support.py)
		- the rows are pairs of pos and neg observations	
		- columns are the difference of the pairs in the binary variables
	classesCSV = CSV classes file (for calculation of constraint coeffcients)

	"""

	print "--- feature selection"
        print " input file:", suppCSV
	
	#read csv data file
	data = pandas.read_csv(suppCSV, header=0, delimiter=",")	
	#VORSICHT! Hier -1, da header und pairs mit drin!
	nbrofrows = len(data) #hier habe ich die -1 wieder weggenommen!!!! 
	nbrofcol = len(list(data))-1
	print "  data - number of rows:", nbrofrows
	print "  data - number of columns:", nbrofcol

	#read csv data file
	classes = pandas.read_csv(classesCSV, header=0, delimiter=",")	
	#VORSICHT! Hier -1, da header und pairs mit drin!
	classes_nbrofrows = len(classes)	
	classes_nbrofcol = len(list(classes))-1
	print "  classes - number of rows:", classes_nbrofrows
	print "  classes - number of columns:", classes_nbrofcol
	
	#filename
	originalname = os.path.splitext(suppCSV)[0]
	name = re.sub('\_suppcalc$', '', originalname)
	name = re.sub("2018-2019/AnswerSetLAD/data/IrvineRepository/testMarch19/","",name)

	print "name: ", name

	
	#select features
	#input

	#objective function coefficients u_i (we use the variance of the attribute)
	u = []
	#wir fügen für jede column die varianz/stdabweichung in den vektor u ein
	for ind in range(1,nbrofcol+1):
		u.append(data.iloc[:,ind].std())

	#constraint coefficients c_ij (we use minimum(dist(cutpoint,p),dist(cutpoint,p'))/range attribute)!!!	
	#hier brauchen wir original data set!
	c = np.ones((nbrofrows, nbrofcol+1))
	#so nutzen wir mehrere delimiters
	#fuer cut-points
	delimiters = "<", ">", "="
	regexPattern = '|'.join(map(re.escape, delimiters))
	#TO DO: for each pair
	#fuer pairs
	pair_delim = "(",",",")"
	regexPair = '|'.join(map(re.escape, pair_delim))
	
	for zeile in range(0,nbrofrows):
		print data.iloc[zeile][0]
		obs=re.split(regexPair,data.iloc[zeile][0])
		firstobs = obs[1].strip()
		secondobs = obs[2].strip()
		print "first", firstobs
		print "second", secondobs
	
		#hier rechne ich jetzt 
		#min(abstand(1,5 zu wert von obs 5),abstand(1,5 zu wert von obs 6))/range col 1	
		#TO DO: fuer zwei cut-points: mittelwert
		myhead = list(data)
		spalte = 0
		for col in myhead[1:]:
			entries = re.split(regexPattern,col)
			for ind in range(0,len(entries)):
				if entries[ind]!="":
					if "col" in entries[ind]:
						mycolumn = entries[ind]
						newcolumn = True
						#print "this is the column we talk about:", mycolumn
						#print min(classes[mycolumn])
						#print max(classes[mycolumn])
						#print "RANGE:", abs(min(classes[mycolumn])-max(classes[mycolumn]))
					else:
						#print "and this is the cut-point:", entries[ind]
						#print "distance obs I:", abs(float(entries[ind]) - float(classes[mycolumn][int(firstobs)]))
						#print "distance obs II:",abs(float(entries[ind]) - float(classes[mycolumn][int(secondobs)]))
						#print "FINAL VALUE: (minimum)/(range):", min(abs(float(entries[ind]) - float(classes[mycolumn][int(firstobs)])), abs(float(entries[ind]) - float(classes[mycolumn][int(secondobs)])))/ abs(min(classes[mycolumn])-max(classes[mycolumn]))
						
						if newcolumn == True:
							print "Spalte:", spalte
							spalte = spalte+1
							myvalue=min(abs(float(entries[ind]) - float(classes[mycolumn][int(firstobs)])), abs(float(entries[ind]) - float(classes[mycolumn][int(secondobs)])))/ abs(min(classes[mycolumn])-max(classes[mycolumn]))
							#print myvalue
							final_value = myvalue
							print "this is final:", final_value
						if newcolumn == False:
							#print "wir addieren!"
							mynextvalue=min(abs(float(entries[ind]) - float(classes[mycolumn][int(firstobs)])), abs(float(entries[ind]) - float(classes[mycolumn][int(secondobs)])))/ abs(min(classes[mycolumn])-max(classes[mycolumn]))
							#print "mynextvalue:", mynextvalue
							final_value=(myvalue+mynextvalue)/2
							print "doch nicht! this is final:", final_value
						
						print "zeile", zeile	
						c[zeile][spalte]=final_value
						newcolumn = False
	print c

	#right hand side coefficients (how different should the positive and negative be?) 
	#1 \leq mu \leq HamDist(Omega^+, Omega^-)
	#hier erstmal mit mu=1
	mu = []
	for ind in range(0,nbrofrows):
		mu.append(1)

	#initialize
	y = []
	for ind in range(0,nbrofcol):
		y.append(0)

	s = []
	for ind in range(0,nbrofrows):
		s.append(0)

	#start loop
	while s < mu:	
		#vector mini enthält an stelle j das minimum aus 1 und 1/mu[j]-s[j]
		#hier fehlt ein c_ij im zähler! (durch 1 ersetzt)
		mini = np.zeros((nbrofrows, nbrofcol))
		for rows in range(0,nbrofrows):
			for cols in range(0,nbrofcol):
				mini[rows][cols] = min(1, c[rows][cols]/(mu[rows]-s[rows]))

		#vector f enthält die gewichtete summe der einträge von mini
		f = []
		for i in range(0,nbrofcol):
			f.append(1/u[i]*sum(mini[j][i] for j in range(0,nbrofrows) if (mu[j] - s[j]) > 0))

		#find index of maximum (DEN HABEN WIR GESUCHT!)
		myindex =  f.index(max(f))
		print myindex
	
		#update vectors
		y[myindex]=1

		for ind in range(0,nbrofrows):
			s[ind]=s[ind]+c[ind][myindex]

	print "--- done."
				


if __name__ == '__main__':
      support(*sys.argv[1:])
