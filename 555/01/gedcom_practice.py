import re

# Valid tags specified in project overview; it would be better to store these
# in a separate file.
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

def getTag(line):
    '''Given a GEDCOM line represented as a list, return the tag'''
    
    tag = line[1]

    # Special case for format "0 <xref-id> <tag>"
    if not int(line[0]) and re.search('^@.+@$', tag):
        tag = line[2]
    
    return (tag in validTags) and tag or 'Invalid tag'
    
if __name__ == '__main__':
    import sys, os.path
    
    # Grab the filename off the command-line
    if len(sys.argv) < 2 or not os.path.isfile(sys.argv[1]):
        raise ValueError('GEDCOM filename must be specified.')
        
    with open(sys.argv[1], encoding = 'utf-8') as f:
    
        # Read each line
        for line in f:
        
            # Print the full line as-is
            line = line.rstrip()
            print(line)
            
            line = line.split(None, 2)
            
            # Print the level number
            print(line[0])
            
            # Print the tag (or 'Invalid tag')
            print(getTag(line))