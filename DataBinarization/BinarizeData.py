# -*- coding: utf-8 -*-

import sys
import pandas
import csv
import numpy as np

def binarize(originalCSV,
	     binCSV):
	"""
	User input explained:

 	originalCSV = CSV data file (attributes = columns, observations = rows)
	binCSV = data file name for binary output file
	"""

        print "--- binarize"
        print " input file:", originalCSV

	
	#read csv data file
	data = pandas.read_csv(originalCSV, header=0, delimiter=",")	
	print data
	nbrofrows = len(data)
	print " number of rows:", nbrofrows

	#cutpoints t_s=1/2*(v_(s-1)+v_s)
	sortdata = data.sort_values(by=['col1'])
	sortdata = sortdata.reset_index(drop=True)
	print sortdata

	myindex = 0
	print sortdata['col1']
	for val in sortdata['col1']:
		print "value", val
		exists_pos = False
		exists_neg = False
		exists_pos_next = False
		exists_neg_next = False

		myindex = myindex + 1
		if myindex == nbrofrows:
			break

		val_next=sortdata['col1'].get_value(myindex)
		print "value next", val_next

		#cut-point
		if val != val_next:
			#essential?
			app_val = sortdata['col1'][sortdata['col1']==val]
			print "app_val", app_val
			new_app = sortdata['col1'].loc[sortdata['col1'][sortdata['col1']==val]]
			print "new_app", new_app
			#pos/neg class for val?
			for ind in app_val:
				if sortdata['col0'].get_value(ind) == 1:
					exists_pos = True
					print "exists_pos!", sortdata['col0'].get_value(ind), "index", ind
				if sortdata['col0'].get_value(ind) == 0:
					exists_neg = True
					print "exists_neg!", sortdata['col0'].get_value(ind), "index", ind


			app_val_next = sortdata['col1'][sortdata['col1']==val_next]
			print "app_val_next", app_val_next
			#pos/neg class for val_next?
			for ind in app_val_next:
				if sortdata['col0'].get_value(ind) == 1:
					exists_pos_next = True
					print "exists_pos_next!", sortdata['col0'].get_value(ind), "index", ind
				if sortdata['col0'].get_value(ind) == 0:
					exists_neg_next = True
					print "exists_neg_next!", sortdata['col0'].get_value(ind), "index", ind

			if exists_pos and exists_neg_next:
					cut= 0.5*(val+val_next)
					print "cutpoint:", val, val_next, cut
			if exists_neg and exists_pos_next:
					cut= 0.5*(val+val_next)
					print "cutpoint:" ,val, val_next, cut

	print sortdata['col0']
	print "here it is:", sortdata['col0'].get_value(10)
			
			
		
			

	



        print " binary output file:", binCSV
        print "---"

if __name__ == '__main__':
      binarize(*sys.argv[1:])

