#!/usr/bin/env python3

numbers=0
avg=0

while True:
	inp=input("Please give me a number or the word 'Done': ")
	
	if inp=="Done":
		break
	else:
		x=float(inp)
		avg+=x
		numbers+=1

avg=avg/numbers
print ("The average is %.2f" % (avg))