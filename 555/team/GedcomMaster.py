#!/usr/bin/env python

import GedcomReader as reader
import GedcomStructs as structs
import sys


greader = reader.GedcomReader(sys.argv[1])

greader.parse()


individuals =  structs.ind_struct(greader.parsed)
families = structs.fam_struct(greader.parsed)
