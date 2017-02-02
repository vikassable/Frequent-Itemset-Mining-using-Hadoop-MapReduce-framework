#!/usr/bin/env python

import sys
# stores key and list of values
dict_keys = {}

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input we got from mapper.py
	key, value = line.split('\t')

	# check if key is already exists in dictionary
	if key in dict_keys:
		# add value to the list
		dict_keys[key].append(int(value))
	else:
		# create list for given key
		dict_keys[key] = []
		# add value to the list
		dict_keys[key].append(int(value))

# write output
for key in dict_keys:
	for index in range(0, len(dict_keys[key])-1):
		# sorting list in ascending order
		dict_keys[key].sort()
		for second_index in range(index + 1, len(dict_keys[key])):
			# writing reducer output to STDOUT
			print('%s\t%s\t%s' % ( dict_keys[key][index], dict_keys[key][second_index], key))