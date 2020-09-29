#!/usr/bin/env python3


s=input("Please enter a list in Python list format: ")
print (s, type(s))
l=eval(s)
print (l, type(l))

for n in l:
	print (n+1)