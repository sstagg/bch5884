#!/usr/bin/env python3

import math

def mean_and_sig(seq):
	'''This function will take a sequence of ints or floats and return the mean and standard deviation (assuming that the sequence is a sample of a population)'''
	avg=sum(seq)
	n=len(seq)
	avg=avg/n
	
	sig=0
	for x in seq:
		sig+=(x-avg)**2
	sig=math.sqrt(sig/(n-1))
	return avg, sig

if __name__ == "__main__":
	l=[2,2,7,8,2,8,3,7,3,3]

	print (mean_and_sig(l))