#! /Library/Frameworks/Python.framework/Versions/Current/bin/python

import os, sys
import glob
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import time

from decimal import *


def TIMEWRAP(st):
	
	print time.time()-st, 'seconds.'
	print (time.time()-st)/60., 'minutes.'
	print (time.time()-st)/(3600.), 'hours.'
	print (time.time()-st)/(60.*60.*24.), 'days.'
	return
	
def runSiB(DIR, namel):
	os.chdir(DIR)
	os.system(DIR+'SiB4D '+namel)
	
def FINDDIR(DIR): 
	if not os.path.isdir(DIR):
		os.system("mkdir -v "+DIR)
	return
	
st=time.time()

TIMEWRAP(st)
sys.exit()