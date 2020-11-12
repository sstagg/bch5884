#!/usr/bin/env python3

import sys
import numpy, scipy.optimize , pylab
import math
from optparse import OptionParser

def setupParserOptions():
	parser=OptionParser()
	parser.add_option('--input', dest='input', default='GroEL_high.raw.111.txt', help = "Input file")
	parser.add_option('--rpm', dest='rpm', default=24000, type='int', help="RPM of centrifuge")
	parser.add_option('--velfig', dest='velfig',default='velfig.png', help="Name of the velocity AUC figure that will be output")
	parser.add_option('--vhwfig', dest='vhwfig', default='vhwfig.png', help='Name of the van Holde Weischet figure that will be output')
	parser.add_option('--sdist', dest='sdist', default='sdist.png', help='Name of the S value distribution figure that will be output' )
	parser.add_option('--shist', dest='shist', default='shist.png', help='Name of the S value histogram that will be output')
	parser.add_option('--html', dest='html', default='auc.html', help='HTML file that summarizes results')
	parser.add_option('--outdir', dest='outdir', default='/home.local/bch5887-01/public_html', help='Name of output directory')
	return parser

def parseAUC(AUCfilename):
	"""Parse AUC text file.
Returns dictionary with the following structure.
{ 'radius': <list of radii for each scan>,
  'nscans': <total number of scans>,
  'scans' : <list of dictionaries with timing and absorbance>,
  	scan list takes the form:
		[ { 'timing' : <time for a given scan>, 'absorbance' : <numpy array of absorbance values> },
		  { 'timing' : <time for a given scan>, 'absorbance' : <numpy array of absorbance values> },]
}"""
	AUCfile=open(AUCfilename, 'r')
	timing=[]
	line=AUCfile.readline()
	words=line.split()
	timing=[int(n) for n in words[2:]]
	timing=numpy.array(timing)
	nscans=len(timing)
	
	scans=[{'timing':timing[n],'absorbance':[]} for n in range(nscans)]
	radius=[]
	lines=AUCfile.readlines()
	AUCfile.close()
	print ("Parsing lines")
	for n in lines:
		words=n.split()
		radius.append(float(words[0]))
		for o in range(nscans):
			scans[o]['absorbance'].append(float(words[o+1]))
		#print radius, scans[0]
	print ("Converting to numpy")
	for scan in scans:
		scan['absorbance']=numpy.array(scan['absorbance'])
	radius=numpy.array(radius)
	return {'radius':radius,'scans':scans,'nscans':nscans}


def divideAbsorbance(absorbance, divisions):
	"""Split an individual scan into equally spaced divisions along absorbance. Returns numpy array of indices for divisions"""
	maxA=absorbance.max()
	minA=absorbance.min()
	interval=(maxA-minA)/divisions
	indices=numpy.zeros(divisions, dtype=int)
	n=0
	searchnumber=interval+minA
	for i in range(absorbance.size):
		if absorbance[i] > searchnumber:
			indices[n]=i
			n+=1
			searchnumber=n*interval+minA
	return indices

def calcApparentSedimentation(aucdict, angvelocity, divisions=50):
	"""Calculate the apparent sed. coefficients.
Return list of 1/time**0.5 and list of arrays of sedimentation divisions."""
#	fig=pylab.figure(2)
	t0=aucdict['scans'][0]['timing']

	sed=[[] for n in range(divisions)]
	root_time=[]
	#calculate 1/time**0.5 and accumulate sedimentation coef. 
	print ("Calculating sedimentation divisions")
	for n in range(4,55):
		indices=divideAbsorbance(aucdict['scans'][n]['absorbance'], divisions=divisions )
#		pylab.plot(aucdict['radius'],aucdict['scans'][n]['absorbance'], figure=fig, hold=True)
#		pylab.savefig("tmp.png")
		root_time.append(1/math.sqrt(aucdict['scans'][n]['timing']))
		for i in range(len(indices)):
			num=math.log(aucdict['radius'][indices[i]]/aucdict['radius'][0])
			denom=(angvelocity**2*(aucdict['scans'][n]['timing']-aucdict['scans'][0]['timing']))
			#print num, denom
			try:
				sb=num/denom
				sb*=10e16		
				sed[i].append(sb)
			except ZeroDivisionError:
				print ("Zero Division Error: num is", num ,"denom is", denom)
	
				sed[i].append(0)
	root_time=numpy.array(root_time)
	return root_time, sed
	
def extrapolateSedimentation(root_time, sed):
	"""Given array of 1/time**0.5 and list of arrays of sed divisions, return list of lines fit to sed divisions."""
	fig2=pylab.figure(4)
	lines=[]
	n=0
	boundaryfrac=[]
	print ("Extrapolating sedimentation lines to infinite time.")
	for s in sed:
		n+=100/len(sed)
		lines.append(fitSedLine(root_time, s))
		boundaryfrac.append(n)
	lines=numpy.array(lines)
	return boundaryfrac,lines


def fitSedLine(time, sedfrac):
	"""Given the time of a scan and the equally spaced divisions, return the linear fit."""
	p=scipy.polyfit(time,sedfrac,1)
	#print p
	return p

#### Plotting functions ####

def plotVelocityData(aucdict,savename=False,fig=False):
	"""Plot all of the scans in an aucdict."""
	if not fig:
		fig=pylab.figure(1)
	for n in range(aucdict['nscans']):
		pylab.plot(aucdict['radius'],aucdict['scans'][n]['absorbance'], figure=fig, hold=True)
	if savename:
		pylab.savefig(savename)

def plotVHW(root_time, sed, lines, savename=False):
	"""Plot boundary fractions and lines."""
	for s in sed:
		pylab.plot(root_time, s, linestyle='None', marker='.', hold=True)
	for line in lines:
		linex=[0,root_time[0]]
		liney=scipy.polyval(line,linex)
		pylab.plot(linex,liney, hold=True)
	if savename:
		pylab.savefig(savename)

def plotSDistribution(lines, boundaryfrac, savename=False):
	"""Plot distribution of S values."""
	pylab.plot(lines[:,1], boundaryfrac, marker=".", hold=True)
	if savename:
		pylab.savefig(savename)

def plotSHistogram(lines, bins=25, savename=False):
	"""Plot histogram of S values."""
	pylab.hist(lines[:,1], bins)
	if savename:
		pylab.savefig(savename)

#### HTML functions ####

def openHTML(f,title):
	f.write("""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
""")
	f.write("<head>\n")
	f.write("<title>%s</title>\n" % title)
	f.write("</head>\n")
	f.write("<body>\n")

def writeHTMLImage(f,title, imgpath):
	f.write('<p class="aucimage">%s</p>\n' % title)
	f.write('<img src="%s" />\n' % imgpath)

def closeHTML(f):
	f.write("</body>\n")
	f.write("</html>\n")
	f.close()	


if __name__ == "__main__":
	rpm=24000
	angvel=rpm*60/(2*math.pi) 
	filename=sys.argv[1]
	f=open(filename,'r')
	aucdict=parseAUC(f)
	#print len(aucdict['radius']), len(aucdict['scans'][0])
	#plotVelocityData(aucdict)
	
	rt, sed= calcApparentSedimentation(aucdict,angvel)
	#for s in sed[0:1]:
	#	pylab.plot(rt, s, marker='x', linestyle='None')
		
	#print indices
	#pylab.plot(aucdict['radius'][indices], aucdict['scans'][0]['absorbance'][indices])
	writeHTML()
	pylab.show()
