from math import*
v=float(input("Entrez la vitesse de la balle: "))
def Distance():
    tetar=(pi/180)*teta
    distance=round((2*(v**2)*cos(tetar)*sin(tetar))/9.8, 2)
    return distance
for x in range(10):
    teta=10*x
    print("A", teta, "degré, la distance équivaut à", Distance())
