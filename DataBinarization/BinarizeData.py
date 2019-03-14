# -*- coding: utf-8 -*-

import sys
import pandas
import csv
import numpy as np
import itertools

def binarize(originalCSV,
	     binCSV,*Interval):
	"""
	User input explained:

 	originalCSV = CSV data file (attributes = columns, observations = rows)
		- the input file needs to have the classes in the first column ('col0');
		- all columns have to be named 'col0', 'col1',...
	binCSV = data file name for binary output file
	Interval = do we want interval variables? if "interval" -> we calculate them, if not -> no 
	"""

        print "--- binarize"
        print " input file:", originalCSV

	
	#read csv data file
	data = pandas.read_csv(originalCSV, header=0, delimiter=",")	
	nbrofrows = len(data)	
	nbrofcol = len(list(data))-1
	print "  number of rows:", nbrofrows
	print "  number of columns:", nbrofcol

	#dataframe for output
	binarydata = pandas.DataFrame(data['col0'])
	binarydata.columns = ['classes']
	
	myheader = list(data)

	#iterate over columns in original data
	for mycol in myheader[1:]:
		#COLUMN1
		#cutpoints t_s=1/2*(v_(s-1)+v_s)
		sortdata = data.sort_values(by=[mycol])
		sortdata = sortdata.reset_index(drop=True)

		myindex = 0		
		cutpoints = []	

		for val in sortdata[mycol]:
			exists_pos = False
			exists_neg = False
			exists_pos_next = False
			exists_neg_next = False

			myindex = myindex + 1
			if myindex == nbrofrows:
				break

			val_next=sortdata[mycol].get_value(myindex)
	

			#cut-point
			if val != val_next:
				#essential?
				appearance = sortdata.index[sortdata[mycol] == val].tolist()
				#pos/neg class for val?
				for ind in appearance:
					if sortdata['col0'].get_value(ind) == 1:
						exists_pos = True
						#print "exists_pos!", sortdata['col0'].get_value(ind), "index", ind
					if sortdata['col0'].get_value(ind) == 0:
						exists_neg = True
						#print "exists_neg!", sortdata['col0'].get_value(ind), "index", ind

				appearance_next = sortdata.index[sortdata[mycol] == val_next].tolist()
				#pos/neg class for val_next?
				for ind in appearance_next:
					if sortdata['col0'].get_value(ind) == 1:
						exists_pos_next = True
						#print "exists_pos_next!", sortdata['col0'].get_value(ind), "index", ind
					if sortdata['col0'].get_value(ind) == 0:
						exists_neg_next = True
						#print "exists_neg_next!", sortdata['col0'].get_value(ind), "index", ind

				if (exists_pos and exists_neg_next) or (exists_neg and exists_pos_next):
						cut= 0.5*(val+val_next)
						cutpoints.append(cut)	

		#LEVEL VARIABLES: each cutpoint creates a new column (x_i>=cutpoint?)
		for point in cutpoints:
			newcolumn = []
			for val in data[mycol]:
				if val >= point:
					entry = 1
				else:
					entry = 0
				newcolumn.append(entry)
			binarydata[str(mycol)+'>='+str(point)]=newcolumn		

		if "interval" in Interval:
		#INTERVAL VARIABLES: new colun for each pair of cut-points (cutpoint1<=x_i<=cutpoint2?)
			for pair in itertools.combinations(cutpoints, 2):
				newcolumn = []
				for val in data[mycol]:
					if pair[0]<=val and val <pair[1]:
						entry = 1
					else: 
						entry = 0
					newcolumn.append(entry)
				binarydata[str(pair[0])+"<="+str(mycol)+"<"+str(pair[1])]=newcolumn
	
	#to csv
	binarydata.to_csv(binCSV, index=False)
	nbrofrows_bin = len(binarydata)
	nbrofcols_bin = len(list(binarydata))-1

	print " "
        print " binary output file:", binCSV
	print "  number of rows:", nbrofrows_bin
	print "  number of columns:", nbrofcols_bin
        print "---"

if __name__ == '__main__':
      binarize(*sys.argv[1:])

