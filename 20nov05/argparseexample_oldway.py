#!/usr/bin/env python3

import sys
import argparse

if len(sys.argv) !=3:
	print ("Usage: argparseexample.py <number1> <number2>")
	print ("I'll add two numbers passed from the command line")
	sys.exit()
	
a=sys.argv[1]
b=sys.argv[2]
sum=a+b

print ("The sum is", sum)