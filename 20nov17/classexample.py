#!/usr/bin/env python3

class C1:
	def __init__(self,value=1):
		self.data=value
	def setdata(self,value):
		self.data=value
	def display(pickle):
		print("The data is",pickle.data)

class C2(C1):
	def setdata2(self,value):
		self.data2=value
	