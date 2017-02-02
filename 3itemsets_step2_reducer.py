#!/usr/bin/env python

import sys
# store 3 itemset as key and list of values
dict_keys = {}

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input we got from mapper.py
	key1, key2, value = line.split('\t')
	# checking for output if it is from 2 item sets or 3 item sets
	if value == 'yes':
		# if key exists in dict then setting is_frequent to true
		if (key1+'\t'+key2) in dict_keys:
			dict_keys[(key1+'\t'+key2)]['is_frequent']= True
		# else creating new entry in dict and setting is_frequent to true
		else:
			dict_keys[(key1+'\t'+key2)] = {}
			dict_keys[(key1+'\t'+key2)]['is_frequent']=True
			dict_keys[(key1+'\t'+key2)]['last_elements']=[]	
	# output from 3 item sets 
	else:
		# if key exists in dict then appending value to the list
		if (key1+'\t'+key2) in dict_keys:
			dict_keys[(key1+'\t'+key2)]['last_elements'].append(value)
		# createing new entry in dict and then appending value to the list
		else:
			dict_keys[(key1+'\t'+key2)] = {}
			dict_keys[(key1+'\t'+key2)]['is_frequent']=False
			dict_keys[(key1+'\t'+key2)]['last_elements']=[]
			dict_keys[(key1+'\t'+key2)]['last_elements'].append(value)

# writing output
for key in dict_keys:
	# checking for is_frequent
	if dict_keys[key]['is_frequent'] is True:
		# for each item in list writing it STDOUT
		for item in dict_keys[key]['last_elements']:
			print('%s\t%s' % (item,key))
