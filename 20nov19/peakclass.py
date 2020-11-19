#!/usr/bin/env python3

import numpy
from matplotlib import pyplot

class Chromat():
	def __init__(self,filename):
		f=open(filename,'r')
		f.readline()
		f.readline()
		f.readline()
		lines=f.readlines()
		f.close()

		time=[]
		absorbance=[]
		for n in lines:
			words=n.split()
			if len(words) == 2:
				time.append(float(words[0]))
				absorbance.append(float(words[1]))
		self.time=numpy.array(time)
		self.absorbance=numpy.array(absorbance)
		
	def plot(self):
		pyplot.plot(self.time,self.absorbance, "ro")
		pyplot.show()


if __name__ == "__main__":
	chromat=Chromat("superose6_50.asc")
	chromat.plot()
