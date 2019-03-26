tab = ['h', 'he', 'li', 'be', 'b', 'c', 'n', 'o', 'f', 'ne', 'na', 'mg', 'al', 'si', 'p', 's', 'cl', 'ar', 'k', 'ca', 'sc', 'ti', 'v', 'cr', 'mn', 'fe', 'co', 'ni', 'cu', 'zn', 'ga', 'ge', 'as', 'se', 'br', 'kr', 'rb', 'sr', 'y', 'zr', 'nb', 'mo', 'tc', 'ru', 'rh', 'pd', 'ag', 'cd', 'in', 'sn', 'sb', 'te', 'i', 'xe', 'cs', 'ba', 'la', 'hf', 'ta', 'w', 're', 'os', 'ir', 'pt', 'au', 'hg', 'tl', 'pb', 'bi', 'po', 'at', 'rn', 'fr', 'ra', 'ac', 'rf', 'db', 'sg', 'bh', 'hs', 'mt', 'ds', 'rg', 'cl', 'ce', 'pf', 'md', 'pm', 'sm', 'eu', 'gd', 'tb', 'dy', 'ho', 'er', 'tm', 'yb', 'lu', 'th', 'pa', 'u', 'np', 'pu', 'am', 'cm', 'bk', 'cf', 'es', 'fm', 'md', 'no', 'lr', '1']

i = 0
p = 0
y = 0
z = 0
wrd = input() + '0'


while wrd.lower()[p] in tab or wrd.lower()[p] + wrd.lower()[p+1] in tab:
	i = 0
	y = 0
	z = 0
	if tab[i] == '1':
		break
	while y == 0:
		if tab[i] == '1':
			y = 1
		elif len(tab[i]) == 1:
			i = i + 1
		else:
			if wrd.lower()[p] + wrd.lower()[p + 1] == tab[i]:
				print(tab[i])
				y = 1
				z = 1
				p = p + 2
			else:
				i = i + 1
	i = 0
	while z == 0:
		if tab[i] == '1':
			z = 1
		elif len(tab[i]) == 2:
			i = i + 1
		else:
			if wrd.lower()[p] == tab[i]:
				print(tab[i])
				z = 1
				p = p + 1
			else:
				i = i + 1
	if wrd[p] == '0':
		break


print('Finish or error')