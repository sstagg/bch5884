#!/usr/bin/env python3

x=99

def f1():
	#print (x)
	x=88
	print ("in function", x)

if __name__ == "__main__":
	print ("before function", x)
	f1()
	print ("after function",x)
