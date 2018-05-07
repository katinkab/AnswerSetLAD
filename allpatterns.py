# -*- coding: utf-8 -*-

import subprocess

def getallpatterns(FnameDATA,
		   FnamePAT,
	           DegLowerBound,
		   DegUpperBound,
		   Hom,
		   Prev):

        print "--- getallpatterns starts calculating..."
        print " data file:", FnameDATA
	print " patterns calculated with:", FnamePAT
	print " lower bound degree:", DegLowerBound
	print " upper bound degree:", DegUpperBound
	print ""
	
	low = int(DegLowerBound)
	high = int(DegUpperBound)
		
	clingo = "Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo"

	print " positive patterns:"

	for deg in range(low,high+1):
		process = subprocess.Popen([clingo, FnameDATA, FnamePAT, "-c sign=1", "-c degree=%i"%deg, "-c homogeneity=%i"%Hom, "-c prevalence=%i"%Prev, "-n 0"], stdout=subprocess.PIPE)
		while True:
  			line = process.stdout.readline()
  			if line !="":
				if "Models" in line:
					print "  degree %i:"%deg, line.rstrip()
				elif "pat" in line:
					print " ", line.rstrip()
  			else:
				print ""
    				break

	print ""
	print " negative patterns:"

	for deg in range(low,high+1):
		process = subprocess.Popen([clingo, FnameDATA, FnamePAT, "-c sign=0", "-c degree=%i"%deg, "-c homogeneity=%i"%Hom, "-c prevalence=%i"%Prev, "-n 0"], stdout=subprocess.PIPE)
		while True:
  			line = process.stdout.readline()
  			if line !="":
				if "Models" in line:
					print "  degree %i:"%deg, line.rstrip()
				elif "pat" in line:
					print " ", line.rstrip()
  			else:
				print ""
    				break

        print "--- getallpatterns done. "
		
getallpatterns("2018/AnswerSetLAD/data/10x10input.asp","2018/AnswerSetLAD/AnswerSetLAD_primepattern.asp", 1, 3, 80, 80)
