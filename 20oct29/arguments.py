#!/usr/bin/env python3

def positional(a,b,c):
	print (a, b, c)

def keyword(a=1,b=1,c=1):
	print (a,b,c)

def pos_and_key(a,b,c=1):
	print (a,b,c)

def mean(name,*nums):
	print (type(nums))
	if len(nums)==0:
		return 0.0
	else:
		avg=sum(nums)/len(nums)
	print (name,avg)
	return avg

def grades(course,**gradebook):
	print (type(gradebook))
	print (gradebook)
	for key in gradebook.keys():
		avg=sum(gradebook[key])/len(gradebook[key])
		print (course, key, avg)


#positional(2,1,3)
#keyword(a=2,b=3)
#pos_and_key(2,1,5)

#m=mean("Scott", 87,88,91,95)
#print (m)

grades("BCH5887", scott=[87,88,91,95], anne=[91,93,95,100], walter=[75,70,78,80])