import re, os.path

class GedcomReader:
	
	# Should be read from a separate plain-text file instead of hard-coded.
	validTags = ('INDI'
				,'NAME'
				,'SEX'
				,'BIRT'
				,'DEAT'
				,'FAMC'
				,'FAMS'
				,'FAM'
				,'MARR'
				,'HUSB'
				,'WIFE'
				,'CHIL'
				,'DIV'
				,'DATE'
				,'TRLR'
				,'NOTE')

	# Given a filename, make sure it exists, it is a GEDCOM file, and it can be
	# opened.
	def __init__(self, filename):
		self.file = None
		
		if not os.path.isfile(filename):
			raise ValueError('File not found: {}'.format(filename))
		
		if not os.path.splitext(filename)[1].lower() == '.ged':
			raise ValueError('File must be a GEDCOM file')
		
		f = open(filename, encoding = 'utf-8')
		
		self.file = f

	# Close the file handle when the object dies. Not sure if this is the best
	# way to handle this; may want to use __enter__ and __exit__ instead.
	def __del__(self):
		if self.file and not self.file.closed:
			self.file.close()

	# Given a GEDCOM line, return the line level
	def getLevel(self, line):
		return int(line.split(None, 1)[0])
	
	# Given a GEDCOM line, return the tag
	def getTag(self, line):
		l = line.rstrip().split(None, 2)
		
		tag = l[1]
		
		if not self.getLevel(line) and re.search('^@.+@$', tag):
			tag = l[2]
		
		return (tag in self.validTags) and tag or 'Invalid tag'
