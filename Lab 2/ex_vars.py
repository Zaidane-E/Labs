# variables - pour stocker des valeurs
# utilisée pour éviter de recalculer des valeurs
# Donnez-les des noms qui pourraient aider a comprendre le code 


# noms des variables valides – compose de lettre, chiffres, caractère souligné (_) (anglais : underscore)
# commence avec lettre ou _
# les noms avec majuscules sont différents des nom sans majuscules

# noms valides - ninja, Ninja, n_i_n_j_a
# noms illegaux - 1337, 1337ninja

# convention Python – jpindre els mots par _
# noms valides - elite_ninja, leet_ninja, ninja_1337
# noms illegaux 1337_ninja



# affectation (anglais: assignment) 
# l’operareur = (egal) est utilisé pour donner des valeurs au variables
# (Note: deux signes egal == est utilisé pour tester l’égalité)

# examples 

mon_nom = "Grace Hopper"
print(mon_nom)

mon_age = 25
print(mon_age)

# anniversaire - ajouter un
mon_age = mon_age + 1
print(mon_age)


# Exemples: Temperature
# transforme de Fahrenheit a Celsius
# c = 5 / 9 * (f - 32)
# utilisez des bons noms des variables !

temp_Fahrenheit = 212

temp_Celsius = 5.0 / 9.0 * (temp_Fahrenheit - 32)

print(temp_Celsius)

# testez-le! 32 Fahrenheit est 0 Celsius, 212 Fahrenheit est 100 Celsius


# Exercise - Solution: transforme de Celsius a Fahrenheit
# f = 9 / 5 * c + 32

temp_Celsius = 100

temp_Fahrenheit = 9.0 / 5.0 * temp_Celsius + 32

print(temp_Fahrenheit)

# testez-le!

