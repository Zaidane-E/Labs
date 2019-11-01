#On demande à l'utilisateur d'entrer une chaine de caracteres
lst=input("Veuillez entrez une plusieurs valeures séparées par des virgules: ")
#On transforme l'entrée de l'utilisateur en liste
lst=list(eval(lst))
#On demande à l'utilisateur d'entrer un entier positif
n=int(input("Veuillez entrez un entier positif: "))

#Prend en parametreune liste et un entier n positif et retourne le nombre de valeures divisible par n
def nombreDivisibles(lst, n):
    #La variable nombre compte le nombres de valeures divisible par n
    nombre=0

    #Boucle for qui verifie pour chaque element de lst s'il est divisible par n
    for i in range(len(lst)):
        #Si la l'element de la liste est divisible par n, on ajoute 1 à nombre
        if lst[i]%n==0:
            nombre=nombre+1

    #La fonction retourne nombre, le nombre de valeures divisibles par n
    return nombre

print(nombreDivisibles(lst, n))
