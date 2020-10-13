#!/usr/bin/env python3

y=15
x=y//2

while x > 1:
	print (x)
	if y%x==0:
		print ("%d has a factor of %d" % (y,x))
		break
	x=x-1
else:
	print ("%d is prime" % (y))