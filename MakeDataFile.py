# -*- coding: utf-8 -*-

def txt2aslad(FnameTXT,
	      FnameASLAD):

        print "--- txt2aslad"
        print " input file:", FnameTXT

	txt_file  = open(FnameTXT, "r") 

	aslad_file= [""]
    	aslad_file+= ["%% Data usable for AnswerSetLAD from input file %s"%FnameTXT]
	aslad_file+= [""]
	
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
			aslad_file+= ["i(%s,%s,%s,%s)."%(str(sign), obsnbr, featnbr, featval)]

	if FnameASLAD==None:
        	return "\n".join(aslad_file)
    	else:
       		with open(FnameASLAD, 'w') as f:
           		f.writelines("\n".join(aslad_file))

	print " number of observations: ", obsnbr
	print " number of features: ", featnbr
	print " output file:", FnameASLAD
        print "---"

txt2aslad("2018/AnswerSetLAD/data/10x10input.txt", "2018/AnswerSetLAD/data/10x10input.aslad")
