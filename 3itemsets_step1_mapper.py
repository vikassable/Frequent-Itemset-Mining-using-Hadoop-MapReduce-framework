#!/usr/bin/env python

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into items
	items = line.split('\t')
	# print output on stdout
	print('%s\t%s' % (items[0],items[1]))