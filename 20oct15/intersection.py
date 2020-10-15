#!/usr/bin/env python3

import random

def intersection(seq1,seq2):
	inboth=[]
	for n in seq1:
		if n in seq2:
			if n not in inboth:
				inboth.append(n)
	return inboth


if __name__=="__main__":	
	s1=[1,2,3,4,4]
	s2=[3,4,5,6]

	inter=intersection(s1,s2)
	print (inter)


	nelements=10
	rands1=[]
	rands2=[]
	for n in range(nelements):
		rands1.append(random.randint(1,5))
		rands2.append(random.randint(1,5))

	inter2=intersection(rands1,rands2)
	print (rands1,rands2)
	inter2.sort()
	print (inter2)