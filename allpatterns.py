# -*- coding: utf-8 -*-

import subprocess

def getallpatterns(FnameDATA,
		   FnamePAT,
	           DegLowerBound,
		   DegUpperBound):

        print "--- getallpatterns"
        print " data file:", FnameDATA
	print " patterns calculated with:", FnamePAT
	print " lower bound degree:", DegLowerBound
	print " upper bound degree:", DegUpperBound
	
	low = int(DegLowerBound)
	high = int(DegUpperBound)

	for deg in range(low,high+1):
		process = subprocess.Popen(["Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo", "2018/KaLAD/data/SPECT_test.kalad", "2018/AnswerSetLAD/AnswerSetLAD_primepattern.asp", "-c sign=0", "-c degree=%i"%deg, "-c homogeneity=100", "-c prevalence=0", "--quiet", "-n 0"], stdout=subprocess.PIPE)
		while True:
  			line = process.stdout.readline()
  			if line !="":
				if "Models" in line:
					print "degree %i:"%deg, line.rstrip()
  			else:
    				break
		
getallpatterns("2018/AnswerSetLAD/data/10x10input.asp","2018/AnswerSetLAD/AnswerSetLAD_primepattern.asp",1,5)
