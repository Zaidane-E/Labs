a=float(input("Pour l'equation de la forme ax²+bx+c, entrez la constante a: "))
b=float(input("Entrez la constante b: "))
c=float(input("Entrez la constante c: "))

if (b**2)-4*a*c==0:
    racines=1
elif (b**2)-4*a*c<0:
    racines=0
elif (b**2)-4*a*c>0:
    racines=2
print("Votre equation admet", racines, "racines.")
