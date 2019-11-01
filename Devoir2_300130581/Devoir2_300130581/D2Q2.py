#Auteur: El Haouari Zaidane
#numéro d'étudiant: 300130581
print("Auteur: El Haouari Zaidane")
print("numéro d'étudiant: 300130581")

#Fonction Fibonacci
def fibonacci(n):
    for x in range(n):
        x=x+(x+1)
        print(x, end=" ")
    return

#Entrée de l'utlisateur et condition(nombre supérieur ou égal à 2)
n=int(input("Entrez le nombre de termes: "))
condition=n>=2

#Boucle de reverification de la condition qui redemande une nouvelle entrée si le nombre indiqué est incorrect
while condition==False:
    n=int(input("Le nombre que vous avez indiqué est incorrect, veuillez entrez le nombre de termes à nouveau: "))
    condition=n>=2
fibonacci(n)
