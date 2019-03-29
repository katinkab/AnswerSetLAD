# -*- coding: utf-8 -*-

import subprocess
import sys
import pandas
import csv
import numpy as np
import os
import re

from SupportSets import Greedy
from SupportSets import PickFeatures_Greedy
from DataBinarization import Disjoint
import MakeDataFile as MakaDataFile
import allpatterns as allpatterns
import ReadAllPatternForCoverCalc as ReadAll

def crossvalidation(binCSV, classesCSV, suppCSV, MyMu, MyN):

	clingo = "Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo"

	#patternfile name
	PATname = "2018-2019/AnswerSetLAD/AnswerSetLAD_prime.asp"
	
	#filename
	originalname = os.path.splitext(binCSV)[0]
	name = re.sub('\_binary$', '', originalname)
	directory = "2018-2019/AnswerSetLAD/data/IrvineRepository/BCW/"
	subdirectory = "mu6/"
	name = re.sub(directory,"",name)
	
	print "----------------------------------------"
	print " name of the data set: ", name


	print "--------- crossvalidation --------------"
	print " binary file: ", binCSV
	print " classes file: ", classesCSV
	print " suppcalc file: ", suppCSV
	keepTXT = directory + subdirectory + name + "_keepcols1.txt"
	print " keepcolumns outfile: ", keepTXT
	shortOutCSV = directory + subdirectory + name+ "_short.csv"
	print " short outfile: ", shortOutCSV
	trainCSV = directory + subdirectory + "train.csv"
	print " trainCSV: ", trainCSV
	trainDisjointOUT = directory + subdirectory + "train_disjoint.csv"
	print " train disjoint out: ", trainDisjointOUT
	print " m =", MyMu
	print " n =", MyN	

	#greedy
	Greedy.support(suppCSV,classesCSV,keepTXT,MyMu)
	#pickfeatures
	PickFeatures_Greedy.pickfeatgreedy(binCSV,keepTXT,shortOutCSV)

	MyData = pandas.read_csv(shortOutCSV)

	# partition in 2/3 (oder was auch immer (n-1)/n)
	floatN = float(MyN)
	myfraction = float((floatN-1)/floatN)
    	row_partition = int(MyData.shape[0] * myfraction)
    	mytrain = MyData[:row_partition]
    	mytest = MyData[row_partition:]
	#write mytrain to csv
	mytrain.to_csv(trainCSV, index=False)
	
	print mytrain
	print mytest

    	#disjoint
	Disjoint.disjoint(trainCSV, trainDisjointOUT)
	#make asp file
	trainDisjointASP = os.path.splitext(trainDisjointOUT)[0]+ ".asp"
	MakaDataFile.txt2asp(trainDisjointOUT,trainDisjointASP)

	#allpatterns
	patternOut = directory + subdirectory + "allprimes.txt"
	nbrFeatures = len(list(mytrain))-1
	allpatterns.getallpatterns(trainDisjointASP, PATname, patternOut,1,nbrFeatures,100,0)
	#make readable input for the asp-files
	Pat_forCover = directory + subdirectory + "allprimes_forcover.asp"
	ReadAll.patternoutput_to_coverinput(patternOut, Pat_forCover)

	#make primecover.asp
	MyPrimecoverASP = "2018-2019/AnswerSetLAD/AnswerSetLAD_primecover.asp"
	Myprocess = subprocess.Popen([clingo, trainDisjointASP, Pat_forCover, MyPrimecoverASP ], stdout=subprocess.PIPE)
	stdout = Myprocess.communicate()[0]
	print 'STDOUT:{}'.format(stdout)
    	primecoverfile= [stdout]
	primecoverOUT = directory + subdirectory + "primecoverOut.asp"
	with open(primecoverOUT, 'w') as f:
           	f.writelines("\n".join(primecoverfile))

	#make primecover_highoccurence.asp
	MyPrimeHighASP = "2018-2019/AnswerSetLAD/AnswerSetLAD_primecover_highoccurence.asp"
	MyHighprocess = subprocess.Popen([clingo, trainDisjointASP, Pat_forCover, MyPrimeHighASP ], stdout=subprocess.PIPE)
	highstdout = MyHighprocess.communicate()[0]
	print 'STDOUT:{}'.format(highstdout)
    	primehighfile= [highstdout]
	primehighOUT = directory + subdirectory + "primecover_highoccOut.asp"
	with open(primehighOUT, 'w') as f:
           	f.writelines("\n".join(primehighfile))

if __name__ == '__main__':
	crossvalidation(*sys.argv[1:])

	
