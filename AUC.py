#!/usr/bin/env python3

from AUClib import *
import sys
import pylab
import os

parser=setupParserOptions()
if len(sys.argv) < 2:
	parser.print_help()
#	parser.error("no options defined")
	sys.exit()
options, args=parser.parse_args()

angvel=options.rpm*60/(2*math.pi) 

#Parse AUC file
aucdict=parseAUC(options.input)

#Change to output directory
os.chdir(options.outdir)
#plot velocity data
plotVelocityData(aucdict, savename=options.velfig)
pylab.clf()

#calculate and plot sedimentation divisions
root_time,sed=calcApparentSedimentation(aucdict,angvel)

#extrapolate sedimentation divisions to infinite time and plot
boundaryfrac, sedlines=extrapolateSedimentation(root_time, sed)
plotVHW(root_time, sed, sedlines, savename=options.vhwfig)
pylab.clf()

#plot S distribution
plotSDistribution(sedlines, boundaryfrac, savename=options.sdist)
pylab.clf()

#plot S histogram
plotSHistogram(sedlines, savename=options.shist)

f=open(options.html,'w')
openHTML(f,"Velocity AUC analysis")
f.write("<h1>Analysis of %s</h1>\n" % options.input)
writeHTMLImage(f, "Velocity AUC", options.velfig)
writeHTMLImage(f, "van Holde Weischet Analysis", options.vhwfig)
writeHTMLImage(f, "S value distribution", options.sdist)
writeHTMLImage(f, "S value histogram", options.shist)
closeHTML(f)
f.close()
#pylab.show()
