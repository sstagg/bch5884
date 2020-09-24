#!/usr/bin/env python3

import sys, random

phrase="Scottz"
lowerphrase=phrase.lower()
#print (lowerphrase)
#sys.exit()

key=random.randint(1,100)
print (key)

for l in lowerphrase:
	i=ord(l)-96
	#print (i)
	new=(i+key%26
	#print (new)
	print (chr(new+96))
