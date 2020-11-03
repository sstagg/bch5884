#!/usr/bin/env python3

def factorial(n):
	print (n)
	if n==0:
		return 1
	else:
		return n*factorial(n-1)

print (factorial(3))