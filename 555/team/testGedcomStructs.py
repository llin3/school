import GedcomStructs as structs
import unittest

class KnownValues(unittest.TestCase):
	known_family_struct = {'@F10@': [[1,'HUSB', '@I10@'], 
					[1,'WIFE', '@I11@'], 
					[1,'CHIL', '@I12@'], 
					[1,'CHIL', '@I13@'], 
					[1,'MARR', '4 JUL 2010']], 
				'@F11@': [[1,'HUSB', '@I12@'], 
					[1,'WIFE', '@I14@']], 
				'@F12@': [[1,'HUSB', '@I15@'], 
					[1,'WIFE', '@I16@'], 
					[1,'CHIL', '@I14@']]}
	
	known_individual_struct = {'@I10@': {'NAME': 'Salvatore /Farino/',
						'GIVN': 'Salvatore',
						'SURN': 'Farino',
						'_MARNM': 'Farino',
						'SEX': 'M',
						'BIRT': '11 FEB 1954',
						'FAMS': '@F10@'},
					'@I11@':{'NAME': 'Debbie /Farino/',
						'GIVN': 'Debbie',
						'SURN': 'Mecca',
						'_MARNM': 'Farino',
						'SEX': 'F',
						'BIRT': '14 MAY 1962',
						'FAMS': '@F10@'}}

	known_parsed_ged_file = [[0, '@I10@', 'INDI'],
				[1, 'NAME', 'Salvatore /Farino/'], 
				[1, 'GIVN', 'Salvatore'], 
				[2, 'SURN', 'Farino'],
				[2, '_MARNM', 'Farino'], 
				[1, 'SEX', 'M'], 
				[1, 'BIRT'], 
				[2, 'DATE', '11 FEB 1954'], 
				[1, 'FAMS', '@F10@'], 
				[0, '@I11@', 'INDI'], 
				[1, 'NAME', 'Debbie /Farino/'], 
				[2, 'GIVN', 'Debbie'], 
				[2, 'SURN', 'Mecca'], 
				[2, '_MARNM', 'Farino'], 
				[1, 'SEX', 'F'], 
				[1, 'BIRT'], 
				[2, 'DATE', '14 MAY 1962'], 
				[1, 'FAMS', '@F10@'], 
				[0, '@F10@', 'FAM'],  
				[1, 'HUSB', '@I10@'], 
				[1, 'WIFE', '@I11@'], 
				[1, 'CHIL', '@I12@'], 
				[1, 'CHIL', '@I13@'], 
				[1, 'MARR'], 
				[2, 'DATE', '4 JUL 2010'], 
				[1, '_CURRENT', 'Y'], 
				[0, '@F11@', 'FAM'], 
				[1, 'HUSB', '@I12@'], 
				[1, 'WIFE', '@I14@'], 
				[1, '_CURRENT', 'Y'], 
				[0, '@F12@', 'FAM'], 
				[1, 'HUSB', '@I15@'], 
				[1, 'WIFE', '@I16@'], 
				[1, 'CHIL', '@I14@'], 
				[1, '_CURRENT', 'Y']]


	def test_fam_struct_known_values(self):
		'''fam_struct should give known result with known input'''
		result = structs.fam_struct(self.known_parsed_ged_file)
		self.assertEqual(result, self.known_family_struct)

	def test_ind_struct_known_values(self):
		'''ind_struct should give known result with known input'''
		result = structs.ind_struct(self.known_parsed_ged_file)
		self.assertEqual(result, self.known_individual_struct)

if __name__ == '__main__':
	unittest.main()	 
