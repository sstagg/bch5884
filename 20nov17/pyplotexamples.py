#!/usr/bin/env python3

import numpy
from matplotlib import pyplot

pyplot.figure(figsize=(10,10),dpi=80)

pyplot.subplot(2,2,1)

X= numpy.linspace(-numpy.pi,numpy.pi, 256, endpoint=True)
C=numpy.cos(X)
S=numpy.sin(X)

pyplot.plot(X,C, color="blue", linewidth=1.0, linestyle="-")
pyplot.plot(X,S, color="green", linewidth=1.0, linestyle="-")

pyplot.subplot(2,2,2)
pyplot.plot(X,S, color="red", linewidth=2, linestyle="--")

pyplot.subplot(2,2,3)
pyplot.plot(X,S, color="red", linewidth=2, linestyle="--")

pyplot.subplot(2,2,4)
pyplot.plot(X,S, color="red", linewidth=2, linestyle="--")
pyplot.xlim(-4,4)
pyplot.ylim(-2,2)

pyplot.xticks(numpy.linspace(-4,4,9, endpoint=True))
pyplot.yticks(numpy.linspace(-2,2,5, endpoint=True))

#pyplot.savefig("sines.png",dpi=144)
pyplot.show()
