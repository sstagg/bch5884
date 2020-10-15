#!/usr/bin/env python3

import sys

pdbfilename=sys.argv[1]

f=open(pdbfilename)
lines=f.readlines()
f.close()

records=[]
massdict={"H":1.01, "C":12.01,"N":14.01,"O":16.0, "P":30.97, "S":32.07,"MG":24.30}
for line in lines:
	atomdict={}
	atomdict['x']=float(line[30:38])
	atomdict['element']=line[76:78].strip()
	atomdict['mass']=massdict[element]
	records.append(atomdict)


print (records)
