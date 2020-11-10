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
parser.add_argument('--add', '-a', action="store_true", default=False, help="sum the numbers")
parser.add_argument('--subtract', '-s', action="store_true", default=False, help="subtract the numbers")
parser.add_argument('--mult', '-m', action="store_true", default=False, help="multiply the numbers")
parser.add_argument('--scale', type=float, default=1, help="scale the results by multiplying by a number")

args=parser.parse_args()
#print (dir(args))
#print (args.numbers)
#print (args.add)

if args.add is True:
	result=sum(args.numbers)
elif args.subtract is True:
	result=-1*sum(args.numbers)
elif args.mult is True:
	result=args.numbers[0]
	for n in args.numbers[1:]:
		result*=n

result=result*args.scale

print ("The result is", result)