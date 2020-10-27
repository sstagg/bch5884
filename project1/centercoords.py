#!/usr/bin/env python3

import sys

def readpdb(pdbfilename):
	"""Parse pdb and return records as a list of dictionaries"""
	pdbfile=open(pdbfilename,'r')
	lines=pdbfile.readlines()
	pdbfile.close()
	
	#parse the pdb
	records=[]
	for line in lines:
		if line[:4]=="ATOM" or line[:6]=="HETATM":
			d={}
			d['rtype']=line[0:6]
			d['atomnumber']=int(line[6:11])
			d['atomtype']=line[12:16]
			d['altloc']=line[16:17]
			d['residue']=line[17:20]
			d['chain']=line[21:22]
			d['residuenumber']=int(line[22:26])
			d['icode']=line[26:27]
			d['x']=float(line[30:38])
			d['y']=float(line[38:46])
			d['z']=float(line[46:54])
			d['occupancy']=float(line[54:60])
			d['tempfact']=float(line[60:66])
			d['element']=line[76:78].strip()
			d['charge']=line[78:80].strip()
			d['mass']=getmass(d['element'])
			records.append(d)
	
	return records

def writepdbline(outfile, d):
	"Write a line to outfile in pdb format. d must be a dictionary containing records for an atom"
	outfile.write("%-6s%5d %-4s%1s%-3s %1s%4d%1s   %8.3f%8.3f%8.3f%6.2f%6.2f          %1s%-2s\n" % (d['rtype'],d['atomnumber'],d['atomtype'],d['altloc'],d['residue'],d['chain'],d['residuenumber'],d['icode'],d['x'],d['y'],d['z'],d['occupancy'],d['tempfact'],d['element'],d['charge']))

def getmass(element):
	"""Determine mass for element type"""
	massdict={"H":1.01, "C":12.01,"N":14.01,"O":16.0,"P":30.97,"S":32.07,"MG":24.30}
	mass=massdict.get(element)
	return mass

def findcenter(atomlist, centype="geom"):
	"""Returns the center of a structure. Must specify "geom" for geometric center or "com" for center of mass."""
	cenx=0
	ceny=0
	cenz=0
	natoms=len(atomlist)
	if centype=="geom":
		for atom in atomlist:
			cenx+=atom['x']
			ceny+=atom['y']
			cenz+=atom['z']
		cenx=cenx/natoms
		ceny=ceny/natoms
		cenz=cenz/natoms
	elif centype=="com":
		totmass=0
		for atom in atomlist:
			cenx+=atom['x']*atom['mass']
			ceny+=atom['y']*atom['mass']
			cenz+=atom['z']*atom['mass']
			totmass+=atom['mass']
		cenx=cenx/totmass
		ceny=ceny/totmass
		cenz=cenz/totmass
	else:
		print ("Center type", centype, "not defined")
		sys.exit()
	return {'x':cenx,'y':ceny,'z':cenz}

def centercoords(atomlist,centerdict, check=False):
	"""Centers atoms by subtracting centerdict. Modifies atomlist"""
	for atom in atomlist:
		atom['x']=atom['x']-centerdict['x']
		atom['y']=atom['y']-centerdict['y']
		atom['z']=atom['z']-centerdict['z']
	if check:
		com=findcenter(atomlist,"com")
		geom=findcenter(atomlist,"geom")
		print ("New center of mass is:", com['x'],com['y'],com['z'])
		print ("New geometric center is:", geom['x'],geom['y'],geom['z'])
	return

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
