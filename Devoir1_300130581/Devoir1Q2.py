#Auteur: Zaidane El Haouari
#Numéro d'étudiant: 300130581

print("Auteur: Zaidane El Haouari")
print("Numéro d'étudiant: 300130581")

jour=int(input("Entrez un entier entre 1 et 7: "))
def jourSemaine(jour):
    if jour==1:
        print("Lundi.")
    elif jour==2:
        print("Mardi.")
    elif jour==3:
        print("Mercredi.")
    elif jour==4:
        print("Jeudi.")
    elif jour==5:
        print("Vendredi.")
    elif jour==6:
        print("Samedi.")
    elif jour==7:
        print("Dimanche.")
    else:
        print("Jour non valide.")
jourSemaine(jour)
