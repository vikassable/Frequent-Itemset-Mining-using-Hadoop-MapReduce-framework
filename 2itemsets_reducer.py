#!/usr/bin/env python

import sys

current_item_1 = None
current_item_2 = None
current_count = 0
item_1 = None
item_2 = None

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input we got from mapper.py
	item_1, item_2, count = line.split('\t')

	# convert count (currently a string) to int
	try:
		count = int(count)
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue

	# this IF-switch only works because Hadoop sorts map output
	# by key (here: word) before it is passed to the reducer
	if current_item_1 == item_1 and current_item_2 == item_2:
		current_count += count
	else:
		if current_item_1 and current_item_2 and current_count >=1000:
			# write result to STDOUT
			print('%s\t%s' % (current_item_1, current_item_2))
		current_count = count
		current_item_1 = item_1
		current_item_2 = item_2

# do not forget to output the last word if needed!
if current_item_1 == item_1 and current_item_2 == item_2 and current_count >=1000:
	print('%s\t%s' % (current_item_1, current_item_2))