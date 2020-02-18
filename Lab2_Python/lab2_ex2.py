#Nom: El Haouari
#Prénom: Zaidane
#Numéro d'étudiant: 300130581

#Fonction
def celsius_en_fahrenheit(temp_celsius):
        "Transforme la température de Celsius en Fahrenheit"
        temp_fahrenheit=((temp_celsius)*(9/5))+32
        return temp_fahrenheit
a="oui"
while a=="oui":
    #Résultats et intérprétation
    t_celsius=float(input("Entrez la température en Celsius: "))
    t_fahrenheit=celsius_en_fahrenheit(t_celsius)
    print(t_celsius, " Celsius est égal à ", t_fahrenheit, "Fahrenheit. \nVoulez vous convertir une autre température?")
    a=input().lower()
