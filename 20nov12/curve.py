#!/usr/bin/env python3

import numpy
from matplotlib import pyplot

f=open("superose6_50.asc")
lines=f.readlines()
f.close()

t=[]
a=[]
for line in lines[3:]:
	words=line.split()
	try:
		t.append(float(words[0]))
		a.append(float(words[1]))
	except:
		print ("could not parse", line)
		continue
#print a

t=numpy.array(t)
a=numpy.array(a)

#pyplot.xlim(0,180)
#pyplot.ylim(0, 2000)
da=numpy.gradient(a)
dda=numpy.gradient(da)
pyplot.plot(t,da)
pyplot.plot(t,a)
pyplot.plot(t,dda)

pyplot.show()
