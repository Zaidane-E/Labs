#Auteur: Zaidane El Haouari
#Numéro d'étudiant: 300130581

print("Auteur: Zaidane El Haouari")
print("Numéro d'étudiant: 300130581")

bureau=75.9
chaise=50.9
imprimante=32.5
scanneur=28.0
article=str(input("Entrez l'article souhaité: "))
quantite=int(input("Entrez la quantité voulue: "))
    
def calculPrix(article, quantite):
    if str.lower(article)=="bureau":
        article=bureau
    elif str.lower(article)=="chaise":
        article=float(chaise)
    elif str.lower(article)=="imprimante":
        article=float(imprimante)
    elif str.lower(article)=="scanneur":
        article=float(scanneur)
    else:
        print("Veuillez entrer un article valide.")
    prix=float(article*quantite)
    print(prix)
    return
calculPrix(article, quantite)

