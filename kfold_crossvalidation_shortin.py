# -*- coding: utf-8 -*-

import subprocess
import sys
import pandas
import csv
import numpy as np
import os
import re
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import ShuffleSplit

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

global interation
global NbrOfFeatures

def importdata(Mydirectory, Mysubdirectory, binCSV, classesCSV, suppCSV, MyMu, nbrfolds, *HaveShortCSV):
	
	#filename
	originalname = os.path.splitext(binCSV)[0]
	
	print "----------------------------------------"
	print " name of the data set: ", originalname


	print "--------- crossvalidation --------------"
	print " binary file: ", binCSV
	print " classes file: ", classesCSV
	print " suppcalc file: ", suppCSV
	keepTXT = Mydirectory + Mysubdirectory + "keepcols.txt"
	print " keepcolumns outfile: ", keepTXT
	shortOutCSV = Mydirectory + Mysubdirectory + "short.csv"
	print " short outfile: ", shortOutCSV
	print " m =", MyMu	

	if not HaveShortCSV:
		print "Features not yet selected for this mu. We calculate:"
		print "-----------------------------------------"
		#greedy
		Greedy.support(suppCSV,classesCSV,keepTXT,MyMu)
		print "-----------------------------------------"
		#pickfeatures
		PickFeatures_Greedy.pickfeatgreedy(binCSV,keepTXT,shortOutCSV)
	else:
		print "We already have a short csv file (with features selected for given mu)!"
		print "this is the path: ", HaveShortCSV
		Myshortfile = pandas.read_csv(HaveShortCSV[0], header=0, delimiter=",")
		Myshortfile.to_csv(shortOutCSV, index=False)
		print "We can use it!"

	#DISJOINT COMPLETE DATA SET
	FullDisjointOUT = Mydirectory + Mysubdirectory + "short_disjoint.csv"
	Disjoint.disjoint(shortOutCSV, FullDisjointOUT)

	MyData = pandas.read_csv(FullDisjointOUT)

	#names of columns
    	myheaders = list(MyData.columns.values)
    
    	#seperate into classes and attributes
    	myattrib = MyData[myheaders[1:]]
    	myclasses = MyData[myheaders[0]].values.ravel()

	#hier wird die globale variable NbrOfFeatures bestimmt
	NbrOfFeatures = len(list(myattrib))
	print " number of features selected:", NbrOfFeatures

    	return myattrib, myclasses, NbrOfFeatures, Mydirectory, Mysubdirectory, nbrfolds


def makeasptraintest(attributes_train, classes_train, attributes_test, classes_test):

	
	print "-----------------------------------------"
	#trainset zusammenfügen
	mytrain = attributes_train
	mytrain.insert(0, column = "classes", value = classes_train)

	#testset zusammenfügen
	mytest = attributes_test
	mytest.insert(0, column = "classes", value = classes_test)

	#write mytrain and mytest to csv
	trainCSV = directory + subdirectory + "train_split" + str(iteration) + ".csv"
	testCSV = directory + subdirectory + "test_split" + str(iteration) + ".csv"
	mytrain.to_csv(trainCSV, index=False)
	mytest.to_csv(testCSV, index=False)

	print "-----------------------------------------"
    	#DISJOINT only train set
	#trainDisjointOUT = directory + subdirectory + "train_split" + str(iteration) + "_disjoint.csv"
	#Disjoint.disjoint(trainCSV, trainDisjointOUT)
	print "-----------------------------------------"
	#make asp file train disjoint
	trainDisjointASP = os.path.splitext(trainCSV)[0]+ ".asp"
	MakaDataFile.txt2asp(trainCSV,trainDisjointASP)
	#make asp file test (no disjoint needed)
	testASP = os.path.splitext(testCSV)[0]+ ".asp"
	MakaDataFile.txt2asp(testCSV,testASP)
	print "-----------------------------------------"

	return trainDisjointASP, testASP

	
def getaccuracy(trainDisjointASP, testASP):

	#allpatterns
	patternOut = directory + subdirectory + "allprimes" + str(iteration) + ".txt"
	#nbrFeatures = len(list(mytrain))-1
	allpatterns.getallpatterns(trainDisjointASP, PATname, patternOut,1,NbrOfFeatures,100,0)
	print "-----------------------------------------"
	#make readable input for the asp-files
	Pat_forCover = directory + subdirectory + "allprimes_forcover"+ str(iteration) + ".asp"
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
	print 'STDOUT:{}'.format(stdout)
	primecoverOUT = directory + subdirectory + "primecoverOut" + str(iteration) + ".asp"
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
	print 'STDOUT:{}'.format(highstdout)
	primehighOUT = directory + subdirectory + "primecover_highoccOut" + str(iteration) + ".asp"
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
	parsedprimecover = directory + subdirectory + "parsed_primecover" + str(iteration) + ".asp"
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
	parsedhighcover = directory + subdirectory + "parsed_primecover_highocc" + str(iteration) + ".asp"
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
	AccuracyPrime = directory + subdirectory + "ACCURACY_primecover" + str(iteration) + ".txt"
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
	AccuracyHighPrime = directory + subdirectory + "ACCURACY_primecover_highocc" + str(iteration) + ".txt"
	with open(AccuracyHighPrime, 'w') as f:
           	f.writelines("\n".join(highprime))
	print "-----------------------------------------"
	print "-----------------------------------------"

if __name__ == '__main__':
	
	#global infos
	clingo = "Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo"
	#patternfile name
	PATname = "2018-2019/AnswerSetLAD/AnswerSetLAD_prime.asp"
	
	attributes, classes, nbrfeatures, mydirectory, mysubdirectory, nbrfolds = importdata(*sys.argv[1:])

	NbrOfFeatures = nbrfeatures

	directory = mydirectory
	subdirectory = mysubdirectory
	
	#define the folds
	#BCW
	#skf = StratifiedShuffleSplit(n_splits=int(nbrfolds), test_size=0.33, train_size=0.66)
	skf = StratifiedKFold(n_splits=int(nbrfolds))
	print "skf:", skf
	
	#to count interations and use for saving the files
	
	iteration = 1

	#k-fold crossvalidation
	for train_index, test_index in skf.split(attributes, classes):
		print "---------------------------------------------"
		print "THIS IS ITERATION ", iteration, "OF THE FOLD."
		print "---------------------------------------------"
		
		x_train, x_test = attributes.loc[train_index], attributes.loc[test_index]
        	y_train, y_test = classes[train_index], classes[test_index]

		mytrainasp, mytestasp = makeasptraintest(x_train, y_train, x_test, y_test)

		getaccuracy(mytrainasp, mytestasp)

		iteration = iteration + 1

	

	
