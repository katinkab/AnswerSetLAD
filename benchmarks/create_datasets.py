# -*- coding: utf-8 -*-

import numpy
import os
import shutil

dir = "Schreibtisch/AnswerSetLAD/benchmarks/randomdata"
if os.path.exists(dir):
	shutil.rmtree(dir)
	print "Existing folder has been removed..."   
os.makedirs(dir)

for rows in range(0,501,50):
	for cols in range(0,rows+1,50):
		if cols!=0 and rows!=0:
			matrix= numpy.random.randint(2, size=(rows, cols+1))
			outfile= open("Schreibtisch/AnswerSetLAD/benchmarks/randomdata/randomdataset"+str(rows)+"x"+str(cols)+".txt", "w")
			for line in matrix:
				for x in line:
					outfile.write(str(x))
					outfile.write(",")
				outfile.write("\n")

for cols in range(0,501,50):
	for rows in range(0,cols+1,50):
		if cols!=0 and rows!=0 and cols!=rows:
			matrix= numpy.random.randint(2, size=(rows, cols+1))
			outfile= open("Schreibtisch/AnswerSetLAD/benchmarks/randomdata/randomdataset"+str(rows)+"x"+str(cols)+".txt", "w")
			for line in matrix:
				for x in line:
					outfile.write(str(x))
					outfile.write(",")
				outfile.write("\n")

print "...and a new folder is filled with new data sets."
