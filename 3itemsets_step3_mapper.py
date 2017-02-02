#!/usr/bin/env python

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into items
	trans_items = line.split(' ')
	# opening candidate file 
	with open('candidates') as check_frequent_3_item_file:
		# for each 3 item set from candidate file chekcing if it is present in a transaction and then output it on STDOUT
		for frequent_item_line in check_frequent_3_item_file:
			frequent_item_line = frequent_item_line.strip()
			frequent_items = frequent_item_line.split('\t')
			# checking presence of 3 itemset in transaction
			if frequent_items[0] in trans_items and frequent_items[1] in trans_items and frequent_items[2] in trans_items:
				print('%s\t%s\t%s\t%s' % (frequent_items[0], frequent_items[1], frequent_items[2],1))