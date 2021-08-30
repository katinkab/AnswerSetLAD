# -*- coding: utf-8 -*-

import subprocess
import sys
import pandas
import csv
import numpy as np
import os
import re

from SupportSets import Support
from SupportSets import Greedy
from SupportSets import PickFeatures_Greedy
from DataBinarization import BinarizeData
from DataBinarization import Disjoint
import MakeDataFile as MakeDataFile

"""
This script executes the full discretisation process (Introduction of Boolean variables, support matrix calculation, greedy feature selection)
"""
#hide future warnings python
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
"""
User input explained:
	originalCSV = direction to input file
	myMU = mu value for greedy algorithm
	Interval = Interval, if interval variables should be calculated (optional)
"""

def importdata(originalCSV,myMu,*Interval):

	originalname = os.path.splitext(originalCSV)[0]	
	if not Interval:
		myInterval = " "
	else:
		myInterval = Interval
	
    	return originalCSV,myMu,myInterval,originalname

if __name__ == '__main__':
	print " --- Discretsation started. ---"
	originalCSV,myMu,myInterval,originalname = importdata(*sys.argv[1:])
	
	binCSV = originalname+"_binary.csv"
	disjointCSV = originalname+"_disjoint.csv"
	suppCSV = originalname+"_support.csv"
	greedyTXT = originalname+"_greedy.txt"
	finalCSV = originalname+"_final.csv"
	finalASP = originalname+".asp"
	
	print "	Introduction of Boolean variables..."
	BinarizeData.binarize(originalCSV,binCSV,myInterval)
	print " DONE."
	print " Disjoint data set..."
	Disjoint.disjoint(binCSV,disjointCSV)
	print " DONE. "
	Support.support(disjointCSV,suppCSV)	
	print " Caluclation of support matrix..."
	print " DONE."
	Greedy.support(suppCSV,originalCSV,greedyTXT,myMu)
	print " Greedy feature selection..."
	print " DONE."
	PickFeatures_Greedy.pickfeatgreedy(binCSV,greedyTXT,finalCSV)
	MakeDataFile.txt2asp(finalCSV,finalASP)
	print " --- Discretisation process completed. ---"
