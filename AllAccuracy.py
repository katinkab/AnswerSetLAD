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


def getALLaccuracy(filename):

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
	parsedprimecover = mydirectory + "parsed_" + str(filename) + ".asp"
	with open(parsedprimecover, 'w') as f:
           	f.writelines("\n".join(primecover_forpredict))
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
	AccuracyPrime = mydirectory + "ACCURACY_" + str(filename) + ".txt"
	with open(AccuracyPrime, 'w') as f:
           	f.writelines("\n".join(accuracyprime))
	print "-----------------------------------------"
	print "-----------------------------------------"
	print "-----------------------------------------"

if __name__ == '__main__':
	
	#global infos
	clingo = "Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo"
	mydirectory = "2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/variance_mu4/prime/"
	
	trainDisjointASP = "2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/variance_mu4/train_split3_disjoint.asp"
	Pat_forCover = "2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/variance_mu4/allprimes_forcover3.asp"

	testASP = "2018-2019/AnswerSetLAD/data/IrvineRepository/BLD/variance_mu4/test_split3.asp"

	for filename in os.listdir(mydirectory):
   		print filename
		primecoverOUT = mydirectory + filename
		getALLaccuracy(filename)
        	continue


	

	
