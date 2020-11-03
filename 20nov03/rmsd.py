#!/usr/bin/env python2

import pdbtools2
import sys

#get the pdb file names
pdbfile1=sys.argv[1]
pdbfile2=sys.argv[2]

#parse the pdb files
atomlist1=pdbtools2.readpdb(pdbfile1)
atomlist2=pdbtools2.readpdb(pdbfile2)

#calculate rmsd
rmsd=pdbtools2.rmsd(atomlist1,atomlist2)

#print out the results
print ("The RMSD between %s and %s is %.3f" % (pdbfile1,pdbfile2,rmsd))