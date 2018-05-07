# -*- coding: utf-8 -*-

import sys

def txt2asp(FnameTXT,
	      FnameASP):
	"""
	User input explained:

 	FnameTXT = TXT data file (0/1 matrix, observations = rows)
	FnameASP = ASP data file name for output
	"""

        print "--- txt2asp"
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

	print " number of observations: ", obsnbr
	print " number of features: ", featnbr
	print " output file:", FnameASP
        print "---"

if __name__ == '__main__':
    txt2asp(*sys.argv[1:])

