# -*- coding: utf-8 -*-

def getallpatterns(FnameDATA,
		   FnamePAT,
	           DegLowerBound,
		   DegUpperBound):

        print "--- getallpatterns"
        print " data file:", FnameDATA
	print " patterns calculated with:", FnamePAT

	pat_file= [""]
    	pat_file+= ["%% All patterns generated with %s from %s from degree %i to %i"%(FnamePAT,FnameDATA,DegLowerBound,DegUpperBound)]
	pat_file+= [""]

		




getallpatterns("2018/AnswerSetLAD/data/10x10input.asp","2018/AnswerSetLAD/AnswerSetLAD_primepattern.asp",0,10)
