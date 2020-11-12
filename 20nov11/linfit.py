#!/usr/bin/env python3

import numpy
from matplotlib import pyplot
import scipy

###create some data
n=1000
x=numpy.linspace(0,15,n,dtype="float64")

a=1.3
b=3

y=a*x+b

noise=numpy.random.normal(0,1,n)
ny=y+noise

###old school regression
meanx=x.mean()
meany=ny.mean()
sx=(x**2).sum()
sy=(ny**2).sum()
sxy=(x*y).sum()

ssxx=sx-n*meanx**2
ssyy=sy-n*meany**2
ssxy=sxy-n*meanx*meany

af=ssxy/ssxx
bf=meany-af*meanx
rsq=ssxy**2/(ssxx*ssyy)

fy=af*x+bf

print (af, bf, rsq)

p=scipy.polyfit(x,ny,1)
print (p)


pyplot.plot(x,ny,'bo')
pyplot.plot(x,fy,'r')
pyplot.show()