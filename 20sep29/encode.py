#!/usr/bin/env python3

import sys, random

#phrase="Scottz"

phrase=input("Please input a phrase to be encrypted: ")
lowerphrase=phrase.lower()

print ("Your phrase is:", phrase)
#print (lowerphrase)
#sys.exit()

key=random.randint(1,100)
#key=0
print ("Your encryption key is: ", key)

newphrase=''
for l in lowerphrase:
	i=ord(l)-96
	#print (i)
	new=(i+key)%26
	#print (new)
	newphrase=newphrase+chr(new+96)
	
print ("Your encoded phrase is: ", newphrase)

decrypted=''
for s in newphrase:
	i=ord(s)-96
	newi=(i-key)%26
	decrypted+=chr(newi+96)

print ("Your decrypted phrase is: ", decrypted)