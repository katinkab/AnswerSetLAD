# -*- coding: utf-8 -*-

import subprocess
import sys

def getallpatterns(FnameDATA,
		   FnamePAT,
	           DegLowerBound,
		   DegUpperBound,
		   Hom=100,
		   Prev=0,
		   *IsQuiet):

        print "--- getallpatterns starts calculating..."
        print " data file:", FnameDATA
	print " patterns calculated with:", FnamePAT
	print " lower bound degree:", DegLowerBound
	print " upper bound degree:", DegUpperBound
	print " homogeneity in percent (lower bound):", Hom
	print " prevalence in percent (lower bound):", Prev
	print ""
	
	low = int(DegLowerBound)
	high = int(DegUpperBound)
	
	homint = int(Hom)
	prevint = int(Prev)
		
	clingo = "Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo"

	print " positive patterns:"

	for deg in range(low,high+1):
		if "quiet" in IsQuiet:
			process = subprocess.Popen([clingo, FnameDATA, FnamePAT, "-c sign=1", "-c degree=%i"%deg, "-c homogeneity=%i"%homint, "-c prevalence=%i"%prevint, "-n 0", "--quiet"], stdout=subprocess.PIPE)
		else:
			process = subprocess.Popen([clingo, FnameDATA, FnamePAT, "-c sign=1", "-c degree=%i"%deg, "-c homogeneity=%i"%homint, "-c prevalence=%i"%prevint, "-n 0"], stdout=subprocess.PIPE)
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
		if "quiet" in IsQuiet:
			process = subprocess.Popen([clingo, FnameDATA, FnamePAT, "-c sign=0", "-c degree=%i"%deg, "-c homogeneity=%i"%homint, "-c prevalence=%i"%prevint, "-n 0", "--quiet"], stdout=subprocess.PIPE)
		else:
			process = subprocess.Popen([clingo, FnameDATA, FnamePAT, "-c sign=0", "-c degree=%i"%deg, "-c homogeneity=%i"%homint, "-c prevalence=%i"%prevint, "-n 0"], stdout=subprocess.PIPE)
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

if __name__ == '__main__':
    getallpatterns(*sys.argv[1:])
