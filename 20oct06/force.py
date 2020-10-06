#!/usr/bin/env python3

l=['Luke','Anakin','Palpatine']

for name in l:
	if name=="Luke":
		force="light"
	elif name=="Palpatine":
		force="dark"
	else:
		force="undetermined"
	print (name,force)