import GedcomReader as ged
import unittest

class GedFileIO(unittest.TestCase):

    def testGedFilenameExt(self):
        '''The user should be notified when the file supplied is not a GEDCOM file'''
        self.assertRaises(ValueError, ged.GedcomReader, 'not a file')
        self.assertRaises(ValueError, ged.GedcomReader, 'testfiles/testGedFilenameExt.txt')
        
        self.assertIsInstance(ged.GedcomReader('testfiles/testGedFilenameExt.ged'), ged.GedcomReader)
    
    def testReadLine(self):
        '''Read a line from a GEDCOM file'''
        greader = ged.GedcomReader('testfiles/testReadLine.ged')
        self.assertIsInstance(greader, ged.GedcomReader)
        
        self.assertEqual(greader.getLine(), 'testReadLine line 1')
        self.assertEqual(greader.getLine(), 'testReadLine line 2')
    
    def testParseLine(self):
        '''Parse a GEDCOM line into data structures'''
        greader = ged.GedcomReader('testfiles/testParseLine.ged')
        self.assertIsInstance(greader, ged.GedcomReader)
        
        greader.parse()
        
        self.assertIsInstance(greader.parsed, list)
        self.assertEqual(len(greader.parsed), 11)
        
        self.assertListEqual(greader.parsed[0], [0, '@I1@', 'INDI'])
        self.assertListEqual(greader.parsed[6], [1, 'BIRT'])
        self.assertListEqual(greader.parsed[9], [0, '@F1@', 'FAM'])
        self.assertListEqual(greader.parsed[7], [2, 'DATE', '30 MAR 1983'])
        self.assertListEqual(greader.parsed[10], [1, 'WIFE', '@I1@'])
    
if __name__ == '__main__':
    unittest.main()