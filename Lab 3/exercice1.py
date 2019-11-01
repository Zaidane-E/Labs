#Entrée
age=int(input("Entrez votre âge: "))

#Condition et résultat booléen
if 18<=age<=55:
    accept=True
else:
    accept=False

#Sortie
if accept==True:
    print("Transaction accepté.")
else:
    print("Transaction refusée.")
