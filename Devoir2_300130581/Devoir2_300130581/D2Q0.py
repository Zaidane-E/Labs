#Auteur: El Haouari Zaidane
#numéro d'étudiant: 300130581
print("Auteur: El Haouari Zaidane")
print("numéro d'étudiant: 300130581")

#Entrée du nombre
nombre = int(input("Entrez un nombre entre 0 et 9999: "))

#Definition de la condition
condition=0<=nombre<=9999

#Fonction qui retourne le nombre de millers, centaines, dizaines et unités
def unites(nombre):
    milliers = (nombre//1000)
    print("Nombre de milliers: ",milliers)
    centaines = (nombre//100)%10
    print("Nombre de centaines: ",centaines)
    dizaines =(nombre//10)%10
    print("Nombre de dizaines: ",dizaines)
    unite =(nombre%10)
    print("Nombre d'unités: ",unite)
    return

#Boucle verifiant la condition (nombre entre 0 et 9999)
if condition==True:
    unites(nombre)
else:
    while condition==False:
        nombre=int(input("Entrez un nombre valide (entre 0 et 9999): "))
        condition=0<=nombre<=9999
        if condition==True:
            unites(nombre)
