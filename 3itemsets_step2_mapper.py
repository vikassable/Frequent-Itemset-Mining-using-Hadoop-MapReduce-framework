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
	if len(items) == 3:
		# writing output from 3 item sets
		print('%s\t%s\t%s' % (items[0],items[1], items[2]))
	else:
		# writing output from 2 item sets, here special value is yes
		print('%s\t%s\t%s' % (items[0],items[1], 'yes'))