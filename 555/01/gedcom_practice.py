from GedcomReader import GedcomReader
    
if __name__ == '__main__':
    import sys
    
    # Grab the filename off the command-line
    if len(sys.argv) < 2:
        raise ValueError('GEDCOM filename must be specified.')

    try:
        ged = GedcomReader(sys.argv[1])
    except Exception as e:
        print('\nError:', e)
        exit()

    # Print each line, its level, and its tag
    for line in ged.file:
        print(line.rstrip())
        print(ged.getLevel(line))
        print(ged.getTag(line))
