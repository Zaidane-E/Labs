#Nom: El Haouari
#Prénom: Zaidane
#Numéro d'étudiant: 300130581

#Fonction
def note_finale(devoirsMoyenne, partiel, examen):
        "La fonction calcule la note finale d'un élève"
        note_finale=(devoirsMoyenne)*(25/100)+(partiel)*(25/100)+(examen)*(50/100)
        return note_finale
a="oui"
while a=="oui":
    #Lire les variable
    note_devoirsMoyenne=float(input("Entrez la Moyenne des devoirs: "))
    note_partiel=float(input("Entrez la note des partiel: "))
    note_examen=float(input("Entrez la note de l'examen: "))
    #Résultats et intérprétation
    if (note_devoirsMoyenne>=0) and (note_partiel>=0) and (note_examen>=0):
        note=note_finale(note_devoirsMoyenne, note_partiel, note_examen)
        print("La note finale est : ", note, "\nVoulez vous calculer une autre Moyenne?")
        a=input().lower()
    else:
        print("Les données sont erronées, veuillez entrez des valeurs postives")
