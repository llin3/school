#!/usr/bin/env python

import sys

def main(argv):
	try:
		f = open(argv[0], 'r')
	except IOError:
		print 'The file either does not exist or is not in the same directory as this script'
		sys.exit(0)
	if argv[0][-4:] != '.ged':
		print 'The file must have the extension .ged'
		sys.exit(0)
	tags = ['INDI', 'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'FAM', 'MAR', 'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'TRLR', 'NOTE']
	valid_tags = set(tags)
	parse_ged(f, valid_tags)


def parse_ged(f, valid_tags):
	for line in f:
		line = line[:-2]
		print line
		print line[0]
		if line[2:5] in valid_tags:
			print line[2:5]
		elif line[2:6] in valid_tags:
			print line[2:6]
		elif line[7:11] in valid_tags:
			print line[7:11]
		else:
			print 'Invalid tag'
		print ''



if __name__ == "__main__":
	main(sys.argv[1:]) 
