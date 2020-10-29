#!/usr/bin/env python3

x=40

def f1():
	global x
	x=80
	print (x)
	
def f2():
	global x
	x=160
	print (x)
	
print (x)
f2()
f1()
f2()
print (x)