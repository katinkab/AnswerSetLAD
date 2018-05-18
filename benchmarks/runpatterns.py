# -*- coding: utf-8 -*-

import sys
import subprocess

def makedata(FnameTXT,
	     FnameDATA):

	print "--- Hello! This is makedata!"
        print " input file:", FnameTXT

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
			index += len(delimiter)    
			asp_file+= ["i(%s,%s,%s,%s)."%(str(sign), obsnbr, featnbr, featval)]

	if FnameASP==None:
        	return "\n".join(asp_file)
    	else:
       		with open(FnameASP, 'w') as f:
           		f.writelines("\n".join(asp_file))

	print " output file:", FnameASP
        print "---"
	

def runpatt(FnameDATA,
	    PatternType,
	    DegLowerBound,
	    DegUpperBound):

	low = int(DegLowerBound)
	high = int(DegUpperBound)
		
	clingo = "Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo"

	print " positive patterns:"

	for deg in range(low,high+1):
		process = subprocess.Popen([clingo, FnameDATA, PatternType, "-c sign=1", "-c degree=%i"%deg, "-c homogeneity=100", "-c prevalence=0", "-n 0", "--quiet"], stdout=subprocess.PIPE)
		while True:
  			line = process.stdout.readline()
  			if line !="":
				if "Models" in line:
					print "  degree %i:"%deg, line.rstrip()
  			else:
				print ""
    				break

	print ""
	print " negative patterns:"

	for deg in range(low,high+1):
		process = subprocess.Popen([clingo, FnameDATA, PatternType, "-c sign=0", "-c degree=%i"%deg, "-c homogeneity=100", "-c prevalence=0", "-n 0", "--quiet"], stdout=subprocess.PIPE)
		while True:
  			line = process.stdout.readline()
  			if line !="":
				if "Models" in line:
					print "  degree %i:"%deg, line.rstrip()
  			else:
				print ""
    				break

        print "--- getallpatterns done. "



if __name__ == '__main__':
	makedata(*sys.argv[1:])
	runpatt(*sys.argv[1:])
