from GedcomReader import GedcomReader
    
if __name__ == '__main__':
    import sys
    
    # Grab the filename off the command-line
    if len(sys.argv) < 2:
        raise ValueError('GEDCOM filename must be specified.')

    ged = GedcomReader(sys.argv[1])

	# Print each line, its level, and its tag
    for line in ged.file:
        print(line.rstrip())
        print(ged.getLevel(line))
        print(ged.getTag(line))
