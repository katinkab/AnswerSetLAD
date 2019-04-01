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




def testvali(trainDisjointASP, Pat_forCover):

	clingo = "Schreibtisch/clingo-4.5.4-linux-x86_64/clingo"

	#patternfile name
	PATname = "Schreibtisch/AnswerSetLAD/AnswerSetLAD_prime.asp"
	
	#filename
	#originalname = os.path.splitext(binCSV)[0]
	#name = re.sub('\_binary$', '', originalname)
	directory = "Schreibtisch/AnswerSetLAD/data/IrvineRepository/HD/"
	subdirectory = "crossvalid_mu3/"
	#name = re.sub(directory,"",name)
	
	print "----------------------------------------"
	#print " name of the data set: ", name



	#make primecover.asp
	primecoverfile = []
	MyPrimecoverASP = "Schreibtisch/AnswerSetLAD/AnswerSetLAD_primecover.asp"
	Myprocess = subprocess.Popen([clingo, trainDisjointASP, Pat_forCover, MyPrimecoverASP, "--quiet=1" ], stdout=subprocess.PIPE)
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
	primecoverOUT = directory + subdirectory + "primecoverOut.asp"
	with open(primecoverOUT, 'w') as f:
           	f.writelines("\n".join(primecoverfile))

	#make primecover_highoccurence.asp
	primehighfile = []
	MyPrimeHighASP = "Schreibtisch/AnswerSetLAD/AnswerSetLAD_primecover_highoccurence.asp"
	MyHighprocess = subprocess.Popen([clingo, trainDisjointASP, Pat_forCover, MyPrimeHighASP, "--quiet=1" ], stdout=subprocess.PIPE)
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
	primehighOUT = directory + subdirectory + "primecover_highoccOut.asp"
	with open(primehighOUT, 'w') as f:
           	f.writelines("\n".join(primehighfile))

	
	#parse for _predict
	print " ----- parsing primecovers for predict ----- "
	MyParser = "Schreibtisch/AnswerSetLAD/ParserCoverPredict.asp"
	#Parse primecover.asp	
	primecover_forpredict = []
	ParsePrimecoverProcess = subprocess.Popen([clingo, trainDisjointASP, Pat_forCover, primecoverOUT, MyParser], stdout=subprocess.PIPE)
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
	ParseHighcoverProcess = subprocess.Popen([clingo, trainDisjointASP, Pat_forCover, primehighOUT, MyParser], stdout=subprocess.PIPE)
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
	print " ----- done. ----- "

	#predict on test data set and get accuracy
	print " ----- calculating prediction accuracy on test set ----- "
	Predict = "Schreibtisch/AnswerSetLAD/AnswerSetLAD_predict.asp"
	accuracyprime = []
	PredictProcess = subprocess.Popen([clingo, trainDisjointASP, parsedprimecover, Predict], stdout=subprocess.PIPE)
	while True:
  		myline = PredictProcess.stdout.readline()
 		if "correct" in myline:
			words = myline.rstrip().split()
			for index in range(0,len(words)):
				accuracyprime += [words[index]+"."]
				print words[index]+"."
			break
	
	

if __name__ == '__main__':
	testvali(*sys.argv[1:])
