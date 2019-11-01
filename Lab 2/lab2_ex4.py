#Nom: El Haouari
#Prénom: Zaidane
#Numéro d'étudiant: 300130581

from math import sqrt

#Fonction
def calcul_surface(cote1, cote2, cote3):
    "La fonction calcule la surface d'un triangle à partir de la longueur de ses trois côtés"
    p=cote1+cote2+cote3
    s=sqrt(p*(p-2*cote1)*(p-2*cote2)*(p-2*cote3))/4
    return s
a="oui"
while a=="oui":
    #Lire les variables
    longueur_cote1=float(input("Entrez la longueur du premier côté : "))
    longueur_cote2=float(input("Entrez la longueur du deuxième côté : "))
    longueur_cote3=float(input("Entrez la longueur du troisième côté : "))
    #Resultats et intérprétation
    if (longueur_cote1>=0) and (longueur_cote2>=0) and (longueur_cote3>=0):
        surface_triangle=calcul_surface(longueur_cote1, longueur_cote2, longueur_cote3)
        print("La surface du triangle est : ", surface_triangle, "\nVoulez vous calculer de nouveau la surface d'un triangle?")
        a=input()
    else:
        print("Les données sont erronées, veuillez entrez des valeurs positives.")
        
