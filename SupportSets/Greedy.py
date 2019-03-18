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

def support(suppCSV,classesCSV,OutFile):
	"""
	User input explained:

	supCSV = CSV input file (for example calculated with Support.py)
		- the rows are pairs of pos and neg observations	
		- columns are the difference of the pairs in the binary variables
	classesCSV = CSV classes file (for calculation of constraint coeffcients)
	OutFile = name for output file

	"""

	print "--- feature selection"
        print " input file:", suppCSV
	
	#read csv data file
	data = pandas.read_csv(suppCSV, header=0, delimiter=",")	
	#VORSICHT! Hier -1, da header und pairs mit drin!
	nbrofrows = len(data) #hier habe ich die -1 wieder weggenommen!!!! 
	nbrofcol = len(list(data))-1
	print "  _suppcalc.csv - number of rows:", nbrofrows
	print "  _suppcalc.csv - number of columns:", nbrofcol

	#read csv data file
	classes = pandas.read_csv(classesCSV, header=0, delimiter=",")	
	#VORSICHT! Hier -1, da header und pairs mit drin!
	classes_nbrofrows = len(classes)	
	classes_nbrofcol = len(list(classes))-1
	print "  _classes.csv - number of rows:", classes_nbrofrows
	print "  _classes.csv - number of columns:", classes_nbrofcol

	#outputfile
	out_file= [""]
    	out_file+= ["%% Columns to keep from file %s"%suppCSV]
	out_file+= [""]

	
	#select features
	#input

	#diese delimiter pakete brauchen wir für u und c
	#fuer cut-points
	delimiters = "<", ">", "="
	regexPattern = '|'.join(map(re.escape, delimiters))
	#TO DO: for each pair
	#fuer pairs
	pair_delim = "(",",",")"
	regexPair = '|'.join(map(re.escape, pair_delim))

	#objective function coefficients u_i (we use the variance of the attribute)
	u = np.zeros(nbrofcol)
	#wir fügen für jede column die varianz/stdabweichung der betroffenen column im original data set in den vektor u ein
	index_u = 0
	for col in list(data)[1:]:
		entries = re.split(regexPattern,col)
		for ind in range(0,len(entries)):
			if entries[ind]!="":
				if "col" in entries[ind]:
					#die aktuelle col
					#mycolumn = entries[ind]
					#print "this is index u:", index_u
					mycolumn = entries[ind]
					#print "this is column:", mycolumn
					#standardabweichung/varianz von column mycolumn in original data file
					vari = classes[mycolumn].std()
					#print "this is standardabweichung:", vari
					u[index_u] = vari
					index_u = index_u+1	

	#constraint coefficients c_ij (we use minimum(dist(cutpoint,p),dist(cutpoint,p'))/range attribute)!!!	
	#hier brauchen wir original data set!

	c = np.zeros((nbrofrows, nbrofcol))
	
	#wir gehen alle paare durch
	for zeile in range(0,nbrofrows):
		#paar
		obs=re.split(regexPair,data.iloc[zeile][0])
		firstobs = obs[1].strip()
		secondobs = obs[2].strip()
		spalte = 0
		#wir gehen alle spalten aus _suppcalc durch
		for col in list(data)[1:]:
			entries = re.split(regexPattern,col)
			#liste des attributes (name)
			myattribute = [s for s in entries if "col" in s][0]
			#spread des attributes
			spread_attribute = abs(min(classes[myattribute])-max(classes[myattribute]))
			#hier eine liste aller cutpoints
			mycutpoints = [s for s in entries if "." in s]
			#min(abstand(cutpoint zu wert von firstobs),abstand(cutpoint zu wert von secondobs))/range attribute	
			if len(mycutpoints) == 1:
				final_value=min(abs(float(mycutpoints[0]) - float(classes[myattribute][int(firstobs)])), abs(float(mycutpoints[0]) - float(classes[myattribute][int(secondobs)])))/ spread_attribute
				c[zeile][spalte] = final_value	
	
			#[fuer zwei cut-points: mittelwert]
			if len(mycutpoints) == 2:
				first_value=min(abs(float(mycutpoints[0]) - float(classes[myattribute][int(firstobs)])), abs(float(mycutpoints[0]) - float(classes[myattribute][int(secondobs)])))/ spread_attribute
				second_value=min(abs(float(mycutpoints[1]) - float(classes[myattribute][int(firstobs)])), abs(float(mycutpoints[1]) - float(classes[myattribute][int(secondobs)])))/ spread_attribute
				final_value=(first_value+second_value)/2
				c[zeile][spalte] = final_value

			spalte = spalte+1

	#right hand side coefficients (how different should the positive and negative be?) 
	#1 \leq mu \leq HamDist(Omega^+, Omega^-)
	#hier erstmal mit mu=1
	mu = []
	for ind in range(0,nbrofrows):
		mu.append(10)

	#initialize
	y = []
	for ind in range(0,nbrofcol):
		y.append(0)

	s = []
	for ind in range(0,nbrofrows):
		s.append(0)

	print "--- columns to keep:"
	#start loop
	while s < mu:	
		#print "s<mu: ", s,"<",mu
		#vector mini enthält an stelle j das minimum aus 1 und 1/mu[j]-s[j]
		mini = np.zeros((nbrofrows, nbrofcol))
		for rows in range(0,nbrofrows):
			for cols in range(0,nbrofcol):
				mini[rows][cols] = min(1, c[rows][cols]/(mu[rows]-s[rows]))
				#print "mini[",rows,"][",cols,"]:", mini[rows][cols]


		#vector f enthält die gewichtete summe der einträge von mini
		f = []
		for i in range(0,nbrofcol):
			#summe
			mysum = sum(mini[j][i] for j in range(0,nbrofrows) if (mu[j] - s[j]) > 0)
			#print "summe für i =", i,":", mysum
			f.append(1/u[i]*mysum)
		#print "vector f:", f

		#hier wandle ich ab: berachte nur die einträge in f die nicht schon gewählt wurden (d.h. bereits in y sind). sonst immer wieder gleiche column ausgewählt.
		#---------------------------------
		keepcols = np.nonzero(y)[0]
		
		for ind in range(0,len(keepcols)):
			f[keepcols[ind]] = 0
		#---------------------------------
		#find index of maximum entry of f (DEN HABEN WIR GESUCHT!)
		myindex =  f.index(max(f))
		print "  ", myindex
		out_file+= ["%s"%str(myindex)]
	
		#update vectors
		y[myindex]=1
		#print "new y:", y

		for ind in range(0,nbrofrows):
			s[ind]=s[ind]+c[ind][myindex]	

	#write file
	with open(OutFile, 'w') as f:
           	f.writelines("\n".join(out_file))

	print "--- done."
				


if __name__ == '__main__':
      support(*sys.argv[1:])
