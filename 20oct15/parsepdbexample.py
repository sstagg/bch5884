#!/usr/bin/env python3

import sys

pdbfilename=sys.argv[1]

f=open(pdbfilename)
lines=f.readlines()
f.close()

records=[]

for line in lines:
	x=float(line[30:38])
	element=line[76:78].strip()
	if element=="C":
		mass=12.01
	elif element=="N":
		mass=14.01
	else:
		mass=None
	records.append([x,element,mass])


print (records)
