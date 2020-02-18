#Fonction qui prend une liste en paramtere et retourne le nombre maximale de valeures identiques qui se suivent
def sequenceMax(lst):
    #la variable sequence compte le nombre d'elements qui se suivent
    sequence=1
    #La variable maximum prend la valeur maximale de sequence après chaque boucle
    maximum=1

    #Boucle qui verifie si deux elements qui se suivent sont identiques
    for i in range(len(lst)-1):
        if lst[i]==lst[i+1]:
            #Si oui, on ajoute 1 à sequence
            sequence=sequence+1
            #Si maximum est inferieur à sequence, maximum prend la valeur de sequence
            if maximum<sequence:
                maximum=sequence
        #Lorsque l'element qui suit n'est pas identique, on reinitialise sequence
        else:
            sequence=1

    #On retourne maximum, le nombres maximale de valeurezs qui se suivent
    return maximum

#On demande à l'utilisateur d'entrer une chaine de caracteres
lst=input("Veuillez entrer une séquence de nombre séparé: ")
#On transforme la chaine de caracteres en lsite
lst=list(eval(lst))
print(sequenceMax(lst))
