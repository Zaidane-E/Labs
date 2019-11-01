#Auteur: Zaidane El Haouari
#Numéro d'étudiant: 300130581

print("Auteur: Zaidane El Haouari")
print("Numéro d'étudiant: 300130581")

from math import pi
monrayon=int(input("Entrez le rayon de votre sphère: "))
def mesure(monrayon):
    surface=4*pi*(monrayon**2)
    volume=(4*pi*(monrayon**3))/3
    print("La surface de votre sphère est : ", surface, ".\n", "Le volume de votre sphère est : ", volume, "." ,sep="")
mesure(monrayon)
