#Demande à l'utlisateur d'entrer une chaine de caracteres
lst=input("Veuillez entrer une séquence de nombre séparé: ")
#Transforme la chaine de caracteres en liste
lst=list(eval(lst))

#Fonction qui prend en parametre une liste et retourne:
#- Vrai dès qu'elle repère une séquence de deux éléments identiques de la liste
#- Faux dans le cas contraire
def sequenceDesDeux(lst):
    #Boucle while qui verifie pour chaque element de la liste si l'element qui le suit est identique
    i=0
    while i<len(lst)-1:
        if lst[i]==lst[i+1]:
            #Si l'element a l'index i est identique à celui en i+1, la fonction retourne vrai
            return True
        i=i+1
    #Si la boucle finie et que aucune séquence de deux elements identiques n'a été detecté, la fonction retourne Faux
    return False
print(sequenceDesDeux(lst))
