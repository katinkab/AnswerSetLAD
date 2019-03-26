# -*- coding: utf-8 -*-

import sys
import pandas
import csv
import numpy as np
import os
import re
import random

"""
This script can be used to find duplicates in rows of data set
"""

def support(classesCSV,disjointCSV):
	"""
	User input explained:

	classesCSV = CSV classes file
	disjointCSV = CSV file for output
	"""

	print "--- remove duplicates"
        print " input file:", classesCSV
	

	#read csv data file
	classes = pandas.read_csv(classesCSV, header=0, delimiter=",")	
	classes_nbrofrows = len(classes)	
	classes_nbrofcol = len(list(classes))-1
	print "  _classes.csv - number of rows:", classes_nbrofrows
	print "  _classes.csv - number of columns:", classes_nbrofcol

	#without repetition in one of the classes
	norepeatclasses=classes.drop_duplicates()
	norepeatclasses_nbrofrows = len(norepeatclasses)	
	norepeatclasses_nbrofcol = len(list(norepeatclasses))-1
	print "  no repetition - number of rows:", norepeatclasses_nbrofrows
	print "  no repetition - number of columns:", norepeatclasses_nbrofcol

	#delete columns that appear in both classes
	disjointclasses=norepeatclasses.drop_duplicates(subset = list(norepeatclasses)[1:], keep=False)
	disjointclasses_nbrofrows = len(disjointclasses)	
	disjointclasses_nbrofcol = len(list(disjointclasses))-1
	print "  disjoint - number of rows:", disjointclasses_nbrofrows
	print "  disjoint - number of columns:", disjointclasses_nbrofcol

	#to CSV
	disjointclasses.to_csv(disjointCSV, index=False)

	print "--- done."
				


if __name__ == '__main__':
      support(*sys.argv[1:])
