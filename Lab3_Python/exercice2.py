natation=1
soccer=2
volleyball=3
ski=4
temp=float(input("Veuillez entrer la température du jour: "))
if temp >=80:
    activite=1
elif 60<=temp<80:
    activite=2
elif 40<=temp<60:
    activite=3
elif temp<40:
    activite=4
if activite==1:
    print("Nous vous recommandons de la Natation.")
elif activite==2:
    print("Nous vous recommandons du Soccer.")
elif activite==3:
    print("Nous vous recommandons du Volleyball")
elif activite==4:
    print("Nous vous recommandons du ski")
    
