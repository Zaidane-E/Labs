#Auteur: Zaidane El Haouari
#Numéro d'étudiant: 300130581

print("Auteur: Zaidane El Haouari")
print("Numéro d'étudiant: 300130581")

def interactionUtilisateur():
    "Fonction qui lit le nom, prénom et identifiant de l'utilisateur"
    prenom=input("Entrez votre prénom: ")
    nom=input("Entrez votre nom: ")
    identifiant=input("Entrez votre identifiant à 4 chiffres: ")
    if len(identifiant)==4 and str(identifiant).isdigit():
        print("Bonjour ", prenom, " ", nom, '''. J'espère que vous allez bien. Bienvenu dans "mon programme". Votre identifiant est: ''', '"', identifiant, '".', sep="")
    else:
        print("Bonjour ", prenom, " ", nom, ". Veuillez vérifier votre identifiant.", sep="")
interactionUtilisateur()
