#!/usr/bin/env python3

import sys

now=int(sys.argv[1])
hoursahead=int(sys.argv[2])

then24=(now + hoursahead % 24)% 24
then12=then24%12
daysahead=hoursahead//24

print("The new time in 24 hour format is", then24, "In 12 hour format is", then12, "With",daysahead, "days elapsed.")
