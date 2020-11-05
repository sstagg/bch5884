#!/usr/bin/env python3

#return the nth element of the fibonacci sequence

def fibonacci(n):
	#returns the nth element of the fibonacci sequence skipping 0 and 1
	if n < 2:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)
		

print (fibonacci(5))