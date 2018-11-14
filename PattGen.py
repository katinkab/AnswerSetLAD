# -*- coding: utf-8 -*-

import sys
import pandas
import csv
import subprocess
import os
import re

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
	print "--- clingo output: ---"

	clingo = "Arbeitsfläche/clingo-4.5.4-linux-x86_64/clingo"
	
	#collect numbers of covered observations
	coverlist = []
	pospattern = ["positive"]	

	print smalldatafile

	#myexpression = re.compile("i\(1,\d+,\d+,\d+\).")
	
	#regexi = re.findall("i\(1,\d+,\d+,\d+\).",workdata)
	#print regexi
	#print type(regexi)

	decision = TRUE			

	while "i(1,13,1,1)." in workdata:

		for word in workdata:
		expr_exists = re.findall("i\(1,\d+,\d+,\d+\).", word)
		print expr_exists
		if not expr_exists:
			print "NO!"
			decision = FALSE
			break

		process = subprocess.Popen([clingo, smalldatafile, patterntype, "--quiet=1"], stdout=subprocess.PIPE)
		for line in iter(process.stdout.readline, ''):  # replace '' with b'' for Python 3
	       		#sys.stdout.write(line)
			for word in line.split():
				if "covered" in word:
					number = word.split(",")
					coverlist.append(int(filter(str.isdigit, number[1])))
				elif "pat" in word:
					pospattern.append(word)
				
		
		print "pattern:", pospattern		
		print " coverage:", coverlist
		print " size:", len(coverlist)

		

		for obs in coverlist:
			#(make a copy of workdata, because i want to iterate AND delete from it)
			for entry in workdata[:]:
				if "i(1,"+str(obs)+"," in entry:
					workdata.remove(entry)

		with open(smalldatafile, "w") as f:
	    		for item in workdata:
				f.write("%s\n" % item)

		coverlist = []
		pospattern = ["positive"]

	
		

if __name__ == '__main__':
      pattgen(*sys.argv[1:])
