#!/usr/bin/env python

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into items
	items = line.split(' ')
	# generating two item sets with first item as key and second item as value
	for index in range(0, len(items)-1):
		for second_index in range(index+1, len(items)):
			print('%s\t%s\t%s' % (items[index], items[second_index], 1))
			