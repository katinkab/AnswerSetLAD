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

	data = input data (binary)
	patterntype = AnswerSetLAD pattern generation file (depending on pattern type that should be used)
		- first verion: use AnswerSetLAD_strongest_nodeg.asp
	"""

	print " "
	print "--- PattGen generates a full pattern cover for you. ---"

	clingo = "Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo"
	
	#read data file to list
	datafile = open(data, "r")
	workdata = datafile.read().split()[9:]

	#copy of data file for deletion process	
	smalldatafile = "2018/AnswerSetLAD/data/workdata.asp"
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

	start_time = time.time()
	posfulltime = 0
	negfulltime = 0

	poswithprint = 0
	negwithprint = 0

	print " "
	print "--- Positive patterns ---"
	#positive patterns
	while decision == True:
		posstart_time = time.time()
		process = subprocess.Popen([clingo, smalldatafile, patterntype, "-c sign=1", "--quiet=1"], stdout=subprocess.PIPE)
		posend_time = time.time()
		posfulltime = posfulltime + posend_time - posstart_time
		
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
		
		posprint_end = time.time()
		poswithprint = poswithprint + posprint_end - posstart_time
		
		print " positive patterns time (in s) till now:", posfulltime
		print " positive patterns time (in s) including printing till now:", poswithprint
		print " "

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

	neg_time = time.time()
	print "--- Negative patterns ---"
	while negdecision == True:
		negstart_time = time.time()
		process = subprocess.Popen([clingo, smalldatafile, patterntype, "-c sign=0", "--quiet=1"], stdout=subprocess.PIPE)
		
		negend_time = time.time()
		negfulltime = negfulltime + negend_time - negstart_time

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
		
		negprint_end = time.time()
		negwithprint = negwithprint + negprint_end - negstart_time

		print " negative patterns time (in s) till now:", negfulltime
		print " negative patterns time (in s) including printing till now:", negwithprint
		print " "
		
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

	negtime = time.time()-neg_time
<<<<<<< HEAD
	print "--- Done in %s seconds. ---" % str(postime+negtime)
	print "--- Positive patterns: %s seconds. ---" % str(postime)
	print "--- Positive patterns only clingo process: %s seconds. --" % str(posfulltime)
	print "--- Negative patterns: %s seconds. ---" % str(negtime)
	print "--- Negative patterns only clingo process: %s seconds. --" % str(negfulltime)

	for i in range(0,100):
		print "Hallo Moritz!"
=======

	print "------------------------------------------------------"
	print "--- Done in %s seconds." % str(postime+negtime)
	print "------------------------------------------------------"
	print "--- Positive patterns: %s seconds." % str(postime)
	print "--- 	only clingo process: %s seconds." % str(posfulltime)
	print "--- 	clingo process + printing: %s seconds." % str(poswithprint)
	print "--- Negative patterns: %s seconds." % str(negtime)
	print "--- 	only clingo process: %s seconds." % str(negfulltime)
	print "--- 	clingo process + printing: %s seconds." % str(negwithprint)
	print "------------------------------------------------------"
>>>>>>> 2bd7893b071d356a9dc3aa7cbd008264be431799

	os.remove(smalldatafile)

if __name__ == '__main__':
      pattgen(*sys.argv[1:])
