from math import*
def Moyenne(liste):
    moyenne=sum(liste)/len(liste)
    return moyenne
valeurs=input("Veuillez entrer une liste des valeurs séparées par des virgules: ")
lst=list(eval(valeurs))
print("Votre liste est: ",lst)
moyenne=Moyenne(lst)
print("Votre moyenne est: ",round(moyenne, 2))
