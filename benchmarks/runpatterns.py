# -*- coding: utf-8 -*-

import sys
import subprocess
import time
import numpy
import os
from os import listdir


def makedata(FnameTXT):

	#checking if observation sets are disjoint

	print "--- Hello! This is runpatterns.py!"
	print " Converting the data to a readable format... "
        print " input file:", FnameTXT

	Name = FnameTXT.split(".")
	FnameASP = Name[0]+".asp"
	
	ModelsInTime.append(Name[0].split("/")[-1])

	txt_file  = open(FnameTXT, "r") 

	asp_file= [""]
    	asp_file+= ["%% Data usable for AnswerSetLAD from input file %s"%FnameTXT]
	asp_file+= [""]
	
	obsnbr=0
	delimiter=","

	for line in txt_file:
		sign = line[0]
		obsnbr = obsnbr+1
		index = 0
		featnbr = 0
		while index < len(line):
			index = line.find(delimiter, index)
			if index == -1: 
				break 
			featnbr = featnbr+1			
			featval = line[index+1]
			if featval!="0" and featval!="1":
				break
			index += len(delimiter)    
			asp_file+= ["i(%s,%s,%s,%s)."%(str(sign), obsnbr, featnbr, featval)]

	if FnameASP==None:
        	return "\n".join(asp_file)
    	else:
       		with open(FnameASP, 'w') as f:
           		f.writelines("\n".join(asp_file))
	
	print " output file:", FnameASP
	
	return FnameASP


	

def runpatt(FnameASP,
	    PatternType,
	    DegLowerBound,
	    DegUpperBound):
	
	print " Generating Patterns..."

	low = int(DegLowerBound)
	high = int(DegUpperBound)
		
	clingo = "Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo"

	start_time = time.time()

	numberofmodels = 0

	#positive patterns

	for deg in range(low,high+1):
		process = subprocess.Popen([clingo, FnameASP, PatternType, "-c sign=1", "-c degree=%i"%deg, "-c homogeneity=100", "-c prevalence=0", "-n 0", "--quiet"], stdout=subprocess.PIPE)
		while True:
  			line = process.stdout.readline()
  			if line !="":
				if "Models" in line:
					numberofmodels = numberofmodels + int(line.split(":")[1])
  			else:
    				break
	#negative patterns

	for deg in range(low,high+1):
		process = subprocess.Popen([clingo, FnameASP, PatternType, "-c sign=0", "-c degree=%i"%deg, "-c homogeneity=100", "-c prevalence=0", "-n 0", "--quiet"], stdout=subprocess.PIPE)
		while True:
  			line = process.stdout.readline()
  			if line !="":
				if "Models" in line:
					numberofmodels = numberofmodels + int(line.split(":")[1])
  			else:
    				break

	endtime = time.time() - start_time

	print(" %s models in %s seconds" %(numberofmodels, endtime))

	ModelsInTime.append((numberofmodels,endtime))

	os.remove(FnameASP)

	print ModelsInTime

	return ModelsInTime




if __name__ == '__main__':
	PatternType = "2018/AnswerSetLAD/AnswerSetLAD_primepattern.asp"
	ModelsInTime = []

	for file in listdir("2018/AnswerSetLAD/benchmarks/randomdata/lessdata"):
		FnameTXT = "2018/AnswerSetLAD/benchmarks/randomdata/lessdata/"+file
		runpatt(makedata(FnameTXT), PatternType,1,3)
	
	print ModelsInTime
