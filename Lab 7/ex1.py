def histogramme(chaine):
    lettres={}
    for c in chaine:
        lettres[c]=lettres.get(c,0)+1
    return lettres

chaine=input('Entrez une chaine de caracteres: ')
histogramme=histogramme(chaine)
for i in sorted(histogramme):
    print((i,histogramme[i]), end='')
