#Auteur: El Haouari Zaidane
#numéro d'étudiant: 300130581
print("Auteur: El Haouari Zaidane")
print("numéro d'étudiant: 300130581")

#Fonction qui retourne :
#True si la chaine de caractere est un palindrome
#False si la chaine de caractere n'est pas un palindrome
def palindrome(chaine):
    
    #Pour ignorer les majuscules et les minuscules, on convertit toute la chaine en minsucule
    chaine=chaine.lower()

    #Boucle for qui vérifie si chaque lettre de chaque coté du mot est la même et qui retourne True ou False
    for i in range(len(chaine)):
        long=len(chaine)
        if chaine[i] == chaine[len(chaine)-1-i]:
            return True
        else:
            return False
print(palindrome("Laval"))
