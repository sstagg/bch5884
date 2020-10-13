#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
	print ("Usage: continuebreak.py <number>")
	print ("________________________________")
	sys.exit()
	
n=int(sys.argv[1])

while n <10:
	n+=1
	print ("First statement",n)
	if n==6:
		break
	if n==4:
		continue
	print ("Second statement",n)
else:
	#pass
	print ("Third statement",n)
print ("Fourth statement")
print ("Fifth statement")
print ("Done!")