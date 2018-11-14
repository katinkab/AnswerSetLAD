# -*- coding: utf-8 -*-

import sys
import subprocess
import os
import re
import time

"""
This script can be used to calculate a full pattern cover based on the precedure "PattGen" by Ryoo et al. (2016)
"""

def pattgen(data,
	    patterntype):
	"""
	User input explained:

	data = input data (binary
)
	patterntype = AnswerSetLAD pattern generation file (depending on pattern type that should be used)
		- first verion: use AnswerSetLAD_strongest_nodeg.asp
	"""

	print "--- PattGen generates a full pattern cover for you. ---"

	clingo = "Schreibtisch/clingo-4.5.4-linux-x86_64/clingo"
	
	#read data file to list
	datafile = open(data, "r")
	workdata = datafile.read().split()[9:]

	#copy of data file for deletion process	
	smalldatafile = "Schreibtisch/AnswerSetLAD/data/workdata.asp"
	with open(smalldatafile, "w") as f:
	    		for item in workdata:
				f.write("%s\n" % item)

	#filename
	mydataname = os.path.basename(data)
	print " data file: ", mydataname

	print " pattern type used for cover:", patterntype
	
	#collect numbers of covered observations
	coverlist = []
	pospattern = []	

	negcoverlist = []
	negpattern = []

	decision = True		
	negdecision = True
	
	print "--- Positive patterns ---"
	#positive patterns
	while decision == True:
		start_time = time.time()
		process = subprocess.Popen([clingo, smalldatafile, patterntype, "-c sign=1", "--quiet=1"], stdout=subprocess.PIPE)
		for line in iter(process.stdout.readline, ''):
			for word in line.split():
				if "covered" in word:
					number = word.split(",")
					coverlist.append(int(filter(str.isdigit, number[1])))
				elif "pat" in word:
					pospattern.append(word)
				
		
		print "pattern:", pospattern		
		#print " coverage:", coverlist
		print " size of coverage:", len(coverlist)

		

		for obs in coverlist:
			#(make a copy of workdata, because i want to iterate AND delete from it)
			for entry in workdata[:]:
				if "i(1,"+str(obs)+"," in entry:
					workdata.remove(entry)

		with open(smalldatafile, "w") as f:
	    		for item in workdata:
				f.write("%s\n" % item)

		coverlist = []
		pospattern = []

		if not workdata:
			decision = False
			break
		for word in workdata:
			expr_exists = re.findall("i\(1,\d+,\d+,\d+\).", word)
			if expr_exists:
				decision = True
				break
			else:
				decision = False
	
	#negative patterns
	postime = time.time()-start_time
	print "--- Negative patterns ---"
	while negdecision == True:
		negstart_time = time.time()
		process = subprocess.Popen([clingo, smalldatafile, patterntype, "-c sign=0", "--quiet=1"], stdout=subprocess.PIPE)
		for line in iter(process.stdout.readline, ''):
			for word in line.split():
				if "covered" in word:
					number = word.split(",")
					negcoverlist.append(int(filter(str.isdigit, number[1])))
				elif "pat" in word:
					negpattern.append(word)
				
		
		print "pattern:", negpattern		
		#print " coverage:", negcoverlist
		print " size of coverage:", len(negcoverlist)

		

		for obs in negcoverlist:
			#(make a copy of workdata, because i want to iterate AND delete from it)
			for entry in workdata[:]:
				if "i(0,"+str(obs)+"," in entry:
					workdata.remove(entry)

		with open(smalldatafile, "w") as f:
	    		for item in workdata:
				f.write("%s\n" % item)

		negcoverlist = []
		negpattern = []

		if not workdata:
			negdecision = False
			break
		for word in workdata:
			expr_exists = re.findall("i\(0,\d+,\d+,\d+\).", word)
			if expr_exists:
				negdecision = True
				break
			else:
				negdecision = False

	negtime = time.time()-negstart_time
	print "--- Done in %s seconds. ---" % str(postime+negtime)

	os.remove(smalldatafile)

if __name__ == '__main__':
      pattgen(*sys.argv[1:])
