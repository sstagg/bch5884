#!/usr/bin/env python3

import sys

names=["Steve", "Elijah", "Arlo", "Frank"]
grades=[95.5,69.3,81.0,89.7]

for i in range(4):
	outstring="The grade for {person:s} is {grade:.1f}%"
#	print (names[i], grades[i])
#	sys.exit()
	print (outstring.format( person=names[i], grade=grades[i] ) )

print ()

for i in range(len(names)):
	outstring="The grade for {person:s} is {grade:.1f}%"
#	print (names[i], grades[i])
#	sys.exit()
	print (outstring.format( person=names[i], grade=grades[i] ) )

print ()

for i,name in enumerate(names):
	outstring="The grade for {person:s} is {grade:.1f}%"
#	print (names[i], grades[i])
#	sys.exit()
	print (outstring.format( person=name, grade=grades[i] ) )

print ("Done!")