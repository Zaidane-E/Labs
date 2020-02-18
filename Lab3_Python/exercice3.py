entier=int(input("Entrez un entier: "))

def estDivisible(entier):
    divisible2=entier%2==0
    divisible3=entier%3==0
    if divisible2 and divisible3:
        divisible=1
    elif divisible2 and not divisible3:
        divisible=2
    elif divisible3 and not divisible2:
        divisible=3
    elif not divisible2 and not divisible3:
        divisible=0
    return divisible

divisible=estDivisible(entier)

if divisible==1:
    print("L'entier est divisible par 2 et par 3.")
elif divisible==2:
    print("L'entier est divisible par 2.")
elif divisible==3:
    print("L'entier est divisible par 3.")
elif divisible==0:
    print("L'entier est divisible ni par 2 ni par 3.")
