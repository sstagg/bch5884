#!/usr/bin/env python3

import sys
import argparse

# if len(sys.argv) !=3:
# 	print ("Usage: argparseexample.py <number1> <number2>")
# 	print ("I'll add two numbers passed from the command line")
# 	sys.exit()
# 	
# a=sys.argv[1]
# b=sys.argv[2]

parser=argparse.ArgumentParser(description="A program to illustrate command line argument parsing") 
parser.add_argument('numbers', type=int, nargs='+', help="a set of numbers")

args=parser.parse_args()
print (dir(args))
print (args.numbers)

#sum=a+b
#print ("The sum is", sum)