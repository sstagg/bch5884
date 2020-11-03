#!/usr/bin/env python3

def mysum(l):
	print (l)
	if not l:
		return 0
	else:
		return l[0]+mysum(l[1:])
		
total=mysum([1,2,3,4,5])

print (total)