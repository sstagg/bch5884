#!/usr/bin/env python3

import sys

pdbname=sys.argv[1]
f=open(pdbname,'r')
lines=f.readlines()

tmplist=[]
for line in lines:
	words=line.split()
	tempfact=float(words[10])
	tmplist.append(tempfact)
	#sys.exit()
f.close()

f=open("tmp.out",'w')
for temp in tmplist:
	s="The temperature factor is {0:6.3f}\n"
	f.write(s.format(temp))
f.close()

print ("Done!")