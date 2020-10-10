#!/usr/bin/env python3

import sys
from matplotlib import pyplot

pdbname=sys.argv[1]
f=open(pdbname,'r')
lines=f.readlines()

tmplist=[]
for line in lines:
	print (line)
	if line[:4] == "ATOM" or line[:6]=="HETATM":
		words=line.split()
		#tempfact=float(words[10])
		tempfact=float(line[60:66])
		tmplist.append(tempfact)
		#sys.exit()
f.close()

f=open("tmp.out",'w')
for temp in tmplist:
	s="The temperature factor is {0:6.3f}\n"
	f.write(s.format(temp))
f.close()

pyplot.plot(tmplist)
pyplot.show()

print ("Done!")