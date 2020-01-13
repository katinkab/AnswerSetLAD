# -*- coding: utf-8 -*-

import sys
import os

#this parser file reads from a binary csv file to parse to a suitable input to the .zpl MIP file

def binary_to_zpl(FnameIN, nbrattr):
	"""
	User input explained:

 	FnameIN = binary CSV file
	"""

        print "--- parsing the binary file for input to .zpl MIP file"
        print " input file:", FnameIN
	print " number of attributes:", nbrattr

	#txt_file  = open(FnameIN, "r") 

	class_file=[]
	attr_file=[]
	negattr_file=[]


	#first row attr_file	
	myfirstline = "|"
    	myfirstline += ''.join((str(i)+",") for i in range(1,int(nbrattr)+1))
	myfirstline = myfirstline[:-1]
	myfirstline += "|"
	attr_file += [myfirstline]

	#first row negattr_file
	mynegline = "|"
	mynegline += ''.join((str(i)+",") for i in range(int(nbrattr)+1,2*int(nbrattr)+1))
	mynegline = mynegline[:-1]
	mynegline += "|"
	negattr_file += [mynegline]

	obsnumber = 1

	with open(FnameIN) as infile:
		next(infile)
		for line in infile:
			#print "Hello",line
			class_file+=["<"+str(obsnumber)+","+str(line[0])+">"+","]
			attr_file+=["|"+str(obsnumber)+"|"+str(line[2:].rstrip('\n'))+"|"]
			first = line.replace(str(0),str(2))
			#print "first:", first
			second = first.replace(str(1),str(0))
			#print "second", second
			negative = second.replace(str(2),str(1))
			#print "negative", negative
			#print "negattr", "|",obsnumber,"|",negative[2:].rstrip('\n'),"|"
			negattr_file+=["|"+str(obsnumber)+"|"+str(negative[2:].rstrip('\n'))+"|"]
			obsnumber = obsnumber +1

	ClassOUT = os.path.splitext(FnameIN)[0] + "_class.mip"
	with open(ClassOUT, 'w') as f:
           		f.writelines("\n".join(class_file))

	AttrOUT = os.path.splitext(FnameIN)[0] + "_attr.mip"
	with open(AttrOUT, 'w') as f:
           		f.writelines("\n".join(attr_file))

	NegAttrOUT = os.path.splitext(FnameIN)[0] + "_negattr.mip"
	with open(NegAttrOUT, 'w') as f:
           		f.writelines("\n".join(negattr_file))
	
	
	print " number of observations:", obsnumber-1
        print "---"

if __name__ == '__main__':
    binary_to_zpl(*sys.argv[1:])
