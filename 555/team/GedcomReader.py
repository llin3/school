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
        
        if not os.path.splitext(filename)[1].lower() == '.ged':
            raise ValueError('File must be a GEDCOM file')
        
        if not os.path.isfile(filename):
            raise ValueError('File not found: {}'.format(filename))
        
        f = open(filename, encoding = 'utf-8')
        
        self.file = f

    # Close the file handle when the object dies. Not sure if this is the best
    # way to handle this; may want to use __enter__ and __exit__ instead.
    def __del__(self):
        if self.file and not self.file.closed:
            self.file.close()

    # Read the next line from the GEDCOM file
    def getLine(self):
        if self.file.closed or not self.file.readable:
            raise ValueError('Unable to read from GEDCOM file')
        
        return self.file.readline().strip()

    # Parse an entire file into a list of lists
    def parse(self):
        if self.file.closed or not self.file.readable:
            raise ValueError('Unable to read from GEDCOM file')
        
        self.file.seek(0)
        self.parsed = []
        
        for line in self.file:
            l = line.strip().split(None, 2)
            l[0] = int(l[0])
            
            self.parsed.append(l)
