#!/usr/bin/env python3

import numpy
from matplotlib import pyplot
import sys

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
		
	def findThresh(self,nsig):
		#find baseline
		i=0
		while self.time[i] < 20.0:
			i+=1 

		#determine threshold
		mean=self.absorbance[:i].mean()
		std=self.absorbance[:i].std()	
		threshold=mean+nsig*std
		return threshold	
	
	def findPeaks(self,threshold):
		peakindices=[]
		peak=threshold
		timepeak=[]
		absorbancepeak=[]
		for n in range(1,self.absorbance.size-1):
			if self.absorbance[n] > threshold:
	#			if absorbance[n] > absorbance[n-1] and absorbance[n] > absorbance[n+1] :
				if self.absorbance[n] > self.absorbance[n-1] and self.absorbance[n] > self.absorbance[n+1] :
					peakindices.append(n)
					timepeak.append(self.time[n])
					absorbancepeak.append(self.absorbance[n])
		self.timepeak=timepeak
		self.absorbancepeak=absorbancepeak
		self.peakindices=peakindices

class Plotter():
	def __init__(self, curveobject):
		pyplot.plot(curveobject.time, curveobject.absorbance)
	def write(self,name):
		pyplot.savefig(name+'.png')
	def show(self):
		pyplot.show()

class PeakPlotter(Plotter):
	def __init__(self, curveobject):
		Plotter.__init__(self,curveobject)
		try:
			pyplot.plot(curveobject.timepeak, curveobject.absorbancepeak,'r+',linestyle='None')
		except AttributeError:
			print ("Please execute 'findPeaks' before PeakPlotter")
	



if __name__ == "__main__":
	chromat=Chromat("superose6_50.asc")
	thresh=chromat.findThresh(100)
	#print (thresh)
	plotter=PeakPlotter(chromat)
	chromat.findPeaks(thresh)
	plotter.write("plot")
	plotter.show()
	
	sys.exit()
	chromat.plot()
