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

#to hide warnings from subprocess clingo
try:
    from subprocess import DEVNULL  
except ImportError:
    DEVNULL = open(os.devnull, 'wb')


def crossvalidation(binCSV, classesCSV, suppCSV, MyMu, MyN):

	clingo = "Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo"

	#patternfile name
	PATname = "2018-2019/AnswerSetLAD/AnswerSetLAD_prime.asp"
	
	#filename
	originalname = os.path.splitext(binCSV)[0]
	name = re.sub('\_binary$', '', originalname)
	directory = "2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/"
	subdirectory = "mu5/"
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
	testCSV = directory + subdirectory + "test.csv"
	print " testCSV: ", testCSV
	trainCSV = directory + subdirectory + "train.csv"
	print " trainCSV: ", trainCSV
	trainDisjointOUT = directory + subdirectory + "train_disjoint.csv"
	print " train disjoint out: ", trainDisjointOUT
	print " m =", MyMu
	print " n =", MyN	

	print "-----------------------------------------"
	#greedy
	Greedy.support(suppCSV,classesCSV,keepTXT,MyMu)
	print "-----------------------------------------"
	#pickfeatures
	PickFeatures_Greedy.pickfeatgreedy(binCSV,keepTXT,shortOutCSV)

	MyData = pandas.read_csv(shortOutCSV)
	print "-----------------------------------------"
	# partition in 2/3 (oder was auch immer (n-1)/n)
	floatN = float(MyN)
	myfraction = float((floatN-1)/floatN)
    	row_partition = int(MyData.shape[0] * myfraction)
    	mytrain = MyData[:row_partition]
    	mytest = MyData[row_partition:]
	#write mytrain and mytest to csv
	mytrain.to_csv(trainCSV, index=False)
	mytest.to_csv(testCSV, index=False)
	
	print mytrain
	print mytest
	print "-----------------------------------------"
    	#disjoint
	Disjoint.disjoint(trainCSV, trainDisjointOUT)
	print "-----------------------------------------"
	#make asp file train disjoint
	trainDisjointASP = os.path.splitext(trainDisjointOUT)[0]+ ".asp"
	MakaDataFile.txt2asp(trainDisjointOUT,trainDisjointASP)
	#make asp file test (no disjoint needed)
	testASP = os.path.splitext(testCSV)[0]+ ".asp"
	MakaDataFile.txt2asp(testCSV,testASP)
	print "-----------------------------------------"

	#allpatterns
	patternOut = directory + subdirectory + "allprimes.txt"
	nbrFeatures = len(list(mytrain))-1
	allpatterns.getallpatterns(trainDisjointASP, PATname, patternOut,1,nbrFeatures,100,0)
	print "-----------------------------------------"
	#make readable input for the asp-files
	Pat_forCover = directory + subdirectory + "allprimes_forcover.asp"
	ReadAll.patternoutput_to_coverinput(patternOut, Pat_forCover)
	print "-----------------------------------------"
	#make primecover.asp
	primecoverfile = []
	MyPrimecoverASP = "2018-2019/AnswerSetLAD/AnswerSetLAD_primecover.asp"
	Myprocess = subprocess.Popen([clingo, trainDisjointASP, Pat_forCover, MyPrimecoverASP, "--quiet=1" ], stdout=subprocess.PIPE, stderr=DEVNULL)
	while True:
  		myline = Myprocess.stdout.readline()
 		if "primecover" in myline:
			words = myline.rstrip().split()
			for index in range(0,len(words)):
				primecoverfile += [words[index]+"."]
				print words[index]+"."
			break
	stdout = Myprocess.communicate()[0]
	print '{}'.format(stdout)
	primecoverOUT = directory + subdirectory + "primecoverOut.asp"
	with open(primecoverOUT, 'w') as f:
           	f.writelines("\n".join(primecoverfile))
	print "-----------------------------------------"
	#make primecover_highoccurence.asp
	primehighfile = []
	MyPrimeHighASP = "2018-2019/AnswerSetLAD/AnswerSetLAD_primecover_highoccurence.asp"
	MyHighprocess = subprocess.Popen([clingo, trainDisjointASP, Pat_forCover, MyPrimeHighASP, "--quiet=1" ], stdout=subprocess.PIPE, stderr=DEVNULL)
	while True:
  		myhighline = MyHighprocess.stdout.readline()
 		if "primecover" in myhighline:
			highwords = myhighline.rstrip().split()
			for index in range(0,len(highwords)):
				primehighfile += [highwords[index]+"."]
				print highwords[index]+"."
			break
	highstdout = MyHighprocess.communicate()[0]
	print '{}'.format(highstdout)
	primehighOUT = directory + subdirectory + "primecover_highoccOut.asp"
	with open(primehighOUT, 'w') as f:
           	f.writelines("\n".join(primehighfile))
	print "-----------------------------------------"
	
	#parse for _predict
	print "----- parsing primecovers for predict"
	MyParser = "2018-2019/AnswerSetLAD/ParserCoverPredict.asp"
	#Parse primecover.asp	
	primecover_forpredict = []
	ParsePrimecoverProcess = subprocess.Popen([clingo, trainDisjointASP, Pat_forCover, primecoverOUT, MyParser], stdout=subprocess.PIPE, stderr=DEVNULL)
	while True:
  		myline = ParsePrimecoverProcess.stdout.readline()
 		if "theorypat" in myline:
			words = myline.rstrip().split()
			for index in range(0,len(words)):
				primecover_forpredict += [words[index]+"."]
			break
	parsedprimecover = directory + subdirectory + "parsed_primecover.asp"
	with open(parsedprimecover, 'w') as f:
           	f.writelines("\n".join(primecover_forpredict))
	#Parse primecover_highocc.asp
	highcover_forpredict = []
	ParseHighcoverProcess = subprocess.Popen([clingo, trainDisjointASP, Pat_forCover, primehighOUT, MyParser], stdout=subprocess.PIPE, stderr=DEVNULL)
	while True:
  		myline = ParseHighcoverProcess.stdout.readline()
 		if "theorypat" in myline:
			words = myline.rstrip().split()
			for index in range(0,len(words)):
				highcover_forpredict += [words[index]+"."]
			break
	parsedhighcover = directory + subdirectory + "parsed_primecover_highocc.asp"
	with open(parsedhighcover, 'w') as f:
           	f.writelines("\n".join(highcover_forpredict))
	print "-----------------------------------------"

	#predict on test data set and get accuracy
	print "----- calculating prediction accuracy on test set"
	Predict = "2018-2019/AnswerSetLAD/AnswerSetLAD_predict.asp"
	#for primecover.asp
	print " statistics for primecover.asp:"
	print " "
	accuracyprime = []
	PredictProcess = subprocess.Popen([clingo, testASP, parsedprimecover, Predict], stdout=subprocess.PIPE, stderr=DEVNULL)
	while True:
  		myline = PredictProcess.stdout.readline()
 		if "correct" in myline:
			words = myline.rstrip().split()
			for index in range(0,len(words)):
				accuracyprime += [words[index]+"."]
				print words[index]+"."
			break
	AccuracyPrime = directory + subdirectory + "ACCURACY_primecover.txt"
	with open(AccuracyPrime, 'w') as f:
           	f.writelines("\n".join(accuracyprime))
	print "-----------------------------------------"
	#for primecover_highocc.asp
	print " statistics for primecover_highoccurence.asp:"
	print " "
	highprime = []
	PredicthighProcess = subprocess.Popen([clingo, testASP, parsedhighcover, Predict], stdout=subprocess.PIPE, stderr=DEVNULL)
	while True:
  		myline = PredicthighProcess.stdout.readline()
 		if "correct" in myline:
			words = myline.rstrip().split()
			for index in range(0,len(words)):
				highprime += [words[index]+"."]
				print words[index]+"."
			break
	AccuracyHighPrime = directory + subdirectory + "ACCURACY_primecover_highocc.txt"
	with open(AccuracyHighPrime, 'w') as f:
           	f.writelines("\n".join(highprime))
	print "-----------------------------------------"
	print "-----------------------------------------"

if __name__ == '__main__':
	crossvalidation(*sys.argv[1:])

	
