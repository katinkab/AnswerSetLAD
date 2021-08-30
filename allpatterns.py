# -*- coding: utf-8 -*-

import subprocess
import sys

def getallpatterns(PATHclingo,
		   FnameDATA,
		   FnamePAT,
	           OutFile,
	           DegLowerBound,
		   DegUpperBound,
		   Hom=100,
		   Prev=0,
		   *IsQuiet):

        print "--- getallpatterns starts calculating..."
	print " path to clingo:", PATHclingo
        print " data file:", FnameDATA
	print " patterns calculated with:", FnamePAT
	print " lower bound degree:", DegLowerBound
	print " upper bound degree:", DegUpperBound
	print " homogeneity in percent (lower bound):", Hom
	print " prevalence in percent (lower bound):", Prev
	print "	output file:", OutFile
	print ""
	
	low = int(DegLowerBound)
	high = int(DegUpperBound)
	
	homint = int(Hom)
	prevint = int(Prev)
		
	outfile= [""]
    	outfile+= ["%% All Patterns of type %s from input file %s for cover calculations"%(FnamePAT, FnameDATA)]
	outfile+= [""]

	print " positive patterns:"
	outfile+= [" positive patterns:"]

	for deg in range(low,high+1):
		if "quiet" in IsQuiet:
			process = subprocess.Popen([PATHclingo, FnameDATA, FnamePAT, "-c sign=1", "-c degree=%i"%deg, "-c homogeneity=%i"%homint, "-c prevalence=%i"%prevint, "-n 0", "--quiet"], stdout=subprocess.PIPE)
		else:
			process = subprocess.Popen([PATHclingo, FnameDATA, FnamePAT, "-c sign=1", "-c degree=%i"%deg, "-c homogeneity=%i"%homint, "-c prevalence=%i"%prevint, "-n 0"], stdout=subprocess.PIPE)
		while True:
  			line = process.stdout.readline()
  			if line !="":
				if "Models" in line:
					#print "  degree %i:"%deg, line.rstrip()
					outfile+= ["  degree %i:"%deg, line.rstrip()]
				elif "pat" in line:
					#print " ", line.rstrip()
					outfile+= [" ", line.rstrip()]
  			else:
				#print ""
				#outfile+= [""]
    				break

	print "...done..."
	outfile+= [""]
	print " negative patterns:"
	outfile+= [" negative patterns:"]

	for deg in range(low,high+1):
		if "quiet" in IsQuiet:
			process = subprocess.Popen([PATHclingo, FnameDATA, FnamePAT, "-c sign=0", "-c degree=%i"%deg, "-c homogeneity=%i"%homint, "-c prevalence=%i"%prevint, "-n 0", "--quiet"], stdout=subprocess.PIPE)
		else:
			process = subprocess.Popen([PATHclingo, FnameDATA, FnamePAT, "-c sign=0", "-c degree=%i"%deg, "-c homogeneity=%i"%homint, "-c prevalence=%i"%prevint, "-n 0"], stdout=subprocess.PIPE)
		while True:
  			line = process.stdout.readline()
  			if line !="":
				if "Models" in line:
					#print "  degree %i:"%deg, line.rstrip()
					outfile+= ["  degree %i:"%deg,line.rstrip()]
				elif "pat" in line:
					#print " ", line.rstrip()
					outfile+= [" ", line.rstrip()]
  			else:
				#print ""
				#outfile+= [""]
    				break

	with open(OutFile, 'w') as f:
           		f.writelines("\n".join(outfile))

        print "--- getallpatterns done. "

if __name__ == '__main__':
    getallpatterns(*sys.argv[1:])
