#!/usr/bin/env python3

import sys
from pdbtools import *


if __name__=="__main__":
	### test for correct usage
	if len(sys.argv) != 3:
		print ('USAGE: centercoords.py <pdbname.pdb> <outpdb.pdb\n_____________________________________________\n\n')
		sys.exit()

	filename=sys.argv[1]
	outfilename=sys.argv[2]
	centertype=input("Please enter 'com' for center of mass or 'geom' for geometric center: ")
	
	atomlist=readpdb(filename)

	### determine center 
	if centertype == "com":
		print ("Determining center of mass")
		center=findcenter(atomlist,centype="com")
	
	elif centertype == "geom":
		print ("Determining geometric center")
		center=findcenter(atomlist,centype="geom")
	else:
		print ("Center type '%s' not defined" % (centertype))
		sys.exit()
	print ("Current center is: ", center)


	###write centered pdb file
	centercoords(atomlist,center,check=True)

	f=open('centered.pdb','w')
	for atom in atomlist:
		writepdbline(f,atom)
	f.close()
