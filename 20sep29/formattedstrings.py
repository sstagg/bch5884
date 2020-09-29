#!/usr/bin/env python3

print ("Here is a formatted string %s!" % ("tada!"))
print ("Here is a formatted string %10s!" % ("tada!"))
print ("Here is a formatted string %-10s!" % ("tada!"))

d={"owner": "Scott", "pet": "Walter"}
print ("The owner of %(pet)s is %(owner)s" % (d))

print ("Here is a float %f" % (1/3))
print ("Here is a float %13f" % (1/3))
print ("Here is a float %.10f" % (1/3))
print ("Here is a float %13.10f" % (1/3))
print ("Here is a float %-13.10f" % (1/3))
print ("Here is a float %5.10f" % (1/3))
print ("Here is a float %+5.2f" % (-1/3))
print ("Here is a float %+5.2f" % (1/3))


print ("Here is an integer %5d" % (3))