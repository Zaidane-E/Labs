from math import*
def MoyMaxMin(liste):
    moyenne=round(sum(liste)/len(liste), 2)
    maximum=max(liste)
    minimum=min(liste)
    return [moyenne, maximum, minimum]
valeurs=input("Veuillez entrer une liste des valeurs séparées par des virgules: ")
lst=list(eval(valeurs))
print("Votre liste est: ",lst)
moyenne_maximum_minimum=MoyMaxMin(lst)
print("Votre moyenne est: ",moyenne_maximum_minimum)
