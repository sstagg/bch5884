#!/usr/bin/env python3

# try:
# 	from scipy import *
# except ImportError:
# 	def printHello:
# 		print ("Hello")
		
numbers=0
avg=0

while True:
	inp=input("Please give me a number or the word 'Done': ")
	
	try:
		x=float(inp)
		avg+=x
		numbers+=1
	except ValueError:
		if inp=="Done":
			break
		else:
			print ("Incorrect value entered. Please enter a number or 'Done'")

try:
	avg=avg/numbers
except ZeroDivisionError:
	print ("Zero numbers entered, please try again")
else:
	#executes if the try completes without an exception
	print ("The average is %.2f" % (avg))