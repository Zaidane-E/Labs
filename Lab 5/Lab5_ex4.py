from math import*
def Moyenne(liste):
    moyenne=sum(liste)/len(liste)
    return moyenne
valeurs=input("Veuillez entrer une liste des valeurs séparées par des virgules: ")
lst=list(eval(valeurs))
print("Votre liste est: ",lst)
moyenne=Moyenne(lst)

def Ecart_type():
    x=0
    for a in range(len(lst)):
        x=x+((lst[a]-moyenne)**2)
    ecart_type=sqrt(x/(len(lst)-1))
    print("Votre ecart type est : ",round(ecart_type, 2))
Ecart_type()
