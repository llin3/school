#!/usr/bin/env/ python

class Ddict(dict):
    def __init__(self, default=None):
        self.default = default

    def __getitem__(self, key):
        if not self.has_key(key):
            self[key] = self.default()
        return dict.__getitem__(self, key)

def fam_struct(parsed_ged):
	families = {}
	date_arg = ''
	for x in parsed_ged:
		if x[1] in ['HUSB', 'WIFE', 'CHIL']:
			families[fam_key].append(x)
		elif x[1] in ['MARR', 'DIV']:
			date_arg = x[1]
		elif x[1] == 'DATE' and date_arg == 'MARR':
			families[fam_key].append([1, 'MARR', x[2]])
			date_arg = ''
		elif x[1] == 'DATE' and date_arg == 'DIV':
			families[fam_key].append([1, 'DIV', x[2]])
			date_arg = ''
		elif len(x) > 2:
			if x[2] == 'FAM':
				fam_key = x[1]
				families[fam_key] = []
	return families

def ind_struct(parsed_ged):
	individuals = Ddict( dict )
	date_arg = ''
	for x in parsed_ged:
		if x[1] in ['NAME', 'GIVN', 'SURN', '_MARNM', 'SEX', 'FAMS', 'FAMC']:
			individuals[indi_key][x[1]] = x[2]
		elif x[1] in ['BIRT', 'DEAT']:
			date_arg = x[1]
		elif x[1] == 'DATE' and date_arg == 'BIRT':
			individuals[indi_key][date_arg] = x[2]
			date_arg = ''
		elif x[1] == 'DATE' and date_arg == 'DEAT':
			individuals[indi_key][date_arg] = x[2]
			date_arg = ''
		elif len(x) > 2:
			if x[2] == 'INDI':
				indi_key = x[1]
	return individuals

def sample_ged_parse():
	ged = [[0, '@I1@', 'INDI'], [1, 'NAME', 'Chris Perro'], [1, 'GIVN', 'Chris'], [1, 'SURN', 'Perro'], [1, 'SEX', 'M'], [1, 'BIRT'], [2, 'DATE', '26 JAN 1988'],[1, 'FAMS', '@F1@'], [1, 'FAMC', '@F2@'],[0,'@F1@', 'FAM'], [1,'HUSB','@I1@'], [1,'WIFE','@I2@'], [1,'_CURRENT','Y'], [0,'@F2@','FAM'], [1,'HUSB','@I3@'], [1,'WIFE','@I4@'], [1,'CHIL','@I1@'], [1,'CHIL','@I5@'], [1,'MARR'], [2,'DATE','27 MAY 1979'], [1,'_CURRENT','Y'], [0,'TRLR']]
	return ged
