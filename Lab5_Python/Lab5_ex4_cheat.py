import statistics
def Ecart_type(liste):
    ecart_type=statistics.stdev(liste)
    return ecart_type
valeurs=input("Veuillez entrer une liste des valeurs séparées par des virgules: ")
lst=list(eval(valeurs))
ecart_type=Ecart_type(lst)
print("Votre ecart type est: ",round(ecart_type, 2))
