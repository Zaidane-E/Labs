S=''' En 1815, M. Charles-François-Bienvenu Myriel était évêque de
Digne. C’était un vieillard d’environ soixante-quinze ans ; il occupait le
siège de Digne depuis 1806. … '''
nS=S.replace('.',' ').replace(',',' ').replace(';', ' ').replace('\n',' ')
print('a)\n', nS)
nS=nS.strip()
print('b)\n', nS)
nS=nS.lower()
print('c)\n', nS)
print('d)', nS.count('de'))
nS=nS.replace('était', 'est')
print('e)\n', nS)
