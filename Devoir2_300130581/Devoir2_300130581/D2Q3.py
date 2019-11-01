#Auteur: El Haouari Zaidane
#numéro d'étudiant: 300130581
print("Auteur: El Haouari Zaidane")
print("numéro d'étudiant: 300130581")

#Fonction qui dessine un triangle isocèle formé du caractère * selon la hauteur donnée
def triangle(hauteur):
    a="*"
    for x in range(hauteur):
        print(a.center(hauteur*2-1))    
        a=a+"**"

#Entrée de l'hauteur du triangle voulue        
hauteur=int(input("Entrez la hauteur du triangle: "))

#Appel de la fonction
triangle(hauteur)
