#Auteur: El Haouari Zaidane
#numéro d'étudiant: 300130581
print("Auteur: El Haouari Zaidane")
print("numéro d'étudiant: 300130581")

#Fonction qui retourne le code de prime du joueur
def obtenirCodePrime(buts,aides,penalites,parties_jouees,annees_de_service):
    "La fonction compare les statistiques du joueur pour retourner le code de prime correspondant"
    if buts>20 or aides>25 or penalites<25:
        if annees_de_service>=5 and parties_jouees>55:
            prime=3
        elif annees_de_service>=5 and parties_jouees<=55:
            prime=2
        elif annees_de_service<5:
            prime=1
    else:
        prime=0
    return prime

#Entrée des statistiques par l'utilisateur et definition de la condition (données positives)
print("Veuillez entrez les statistiques du joueur:")
buts=int(input("Nombre de buts: "))
aides=int(input("Nombre d'aides: "))
penalties=int(input("Nombre de pénalties: "))
parties_jouees=int(input("Nombre de parties jouées: "))
annees_de_service=int(input("Nombre d'années de servoce: "))
condition=buts>=0 and aides>=0 and penalties>=0 and parties_jouees>=0 and annees_de_service >=0

#Boucle qui vérifie la condition et qui redemande à l'utilisateur une nouvelle entrée si la condition n'est pas respectée
while condition==False:
    print("Les statistiques entrées ne sont pas valides, veuillez entrez vérifier vos données et essayer à nouveau")
    buts=int(input("Nombre de buts: "))
    aides=int(input("Nombre d'aides: "))
    penalties=int(input("Nombre de pénalties: "))
    parties_jouees=int(input("Nombre de parties jouées: "))
    annees_de_service=int(input("Nombre d'années de servoce: "))
    condition=buts>=0 and aides>=0 and penalties>=0 and parties_jouees>=0 and annees_de_service >=0

print("Le code de prime du joueur est:", obtenirCodePrime(buts,aides,penalties,parties_jouees,annees_de_service))
