# Jeu de cartes appelé "Pouilleux" 

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente tous les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)

def donne_cartes(p):
    '''(list of str)-> tuple of (list of str,list of str)

    Retournes deux listes qui représentent les deux mains des cartes.  
    Le donneur donne une carte à l'autre joueur, une à lui-même,
    et ça continue jusqu'à la fin du paquet p.
    '''
    donneur=[]
    autre=[]
    
    #On définit la variable x prend deux valeurs: 0 et 1
    x=0

    #On crée une boucle for pour donner une carte à chaque joueur
    for i in range(len(p)):
        #Si x=0, une carte est donnée à donneur (Robot)
        if x==0:
            donneur.append(p[i])
            #Après avoir donné une carte à donneur (Robot), x prend la valeur 1
            x=x+1
        #Si x=1, une carte est donnée à autre (Humain)
        else:
            autre.append(p[i])
            #Après avoir donné une carte à autre (Humain), x prend la valeur 0
            x=x-1
     
    return (donneur, autre)


def elimine_paires(l):
    '''
    (list of str)->list of str

    Retourne une copy de la liste l avec tous les paires éliminées 
    et mélange les éléments qui restent.

    Test:
    (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
    >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
    ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
    >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
    ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''
    #On trie d'abord la liste des cartes du joueur
    l.sort()
    #Resultat copie la liste triée
    resultat=l.copy()
    
    #On définit n, le nombre de cartes qui sont éliminées
    n=0
    #Boucle while qui elmine deux mêmes cartes qui se suivent
    i=0
    while i<len(l)-1:
        #Si 2 carte sont supprimées, l'index doit avancer de 2:
        if l[i][0]==l[i+1][0]:
            #Puisque la liste se raccourcie, on elimine deux carte sans changer l'index
            #On retranche n à l'index car la liste se raccourcie de n (nombre de cartes supprimées) quand deux memes cartes se suivent
            resultat.pop(i-n) and resultat.pop(i-n)
            n=n+2
            #On ajoute i=i+1 pour que l'index avance de 2
            i=i+1
        i=i+1
    #On mélange la liste des cartes
    random.shuffle(resultat)
    return resultat


def affiche_cartes(p):
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''
    #On transforme la liste en chaine de caractère
    #On remplace les virgules par des espaces
    print(','.join(p).replace(',',' '))
    

def entrez_position_valide(n):
    '''
    (int)->int
    Retourne un entier du clavier, de 1 à n (1 et n inclus).
    Continue à demander si l'usager entre un entier qui n'est pas dans l'intervalle [1,n]
    
    Précondition: n>=1
    '''
    #On demande à l'utilisateur d'entrer la position
    position=input("J'ai {0} cartes. Si 1 est la position de ma première carte et {0} la position de ma dernière carte, laquelle de mes cartes voulez-vous? SVP entrez un entier de 1 à {0} : ".format(n))
    #On crée une condition pour la valeur position:
    #Position doit être un chiffre entre 1 et n
    condition=position.isdigit() and 1<=int(position)<=n

    #Boucle while qui redemande à l'utilisateur d'entrer une valeur si la condition n'est pas respectée
    while condition==False:
        position=input("Position invalide. SVP entrez un entier de 1 à {0}: ".format(n))
        condition=position.isdigit() and 1<=int(position)<=n

    return int(position)
     

def joue():
    '''()->None
    Cette fonction joue le jeu'''
    
    p=prepare_paquet()
    melange_paquet(p)
    tmp=donne_cartes(p)
    donneur=tmp[0]
    humain=tmp[1]

    print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
    print("Votre main est:")
    affiche_cartes(humain)
    print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
    print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
    attend_le_joueur()
    print(45*"*")
     
    donneur=elimine_paires(donneur)
    humain=elimine_paires(humain)

    #On définit la variable tour qui prend:
    #0 si c'est le tour de Robot
    #1 si c'est le tour de Humain
    tour=1

    #Boucle qui continue le jeu tant que aucun joueur n'a fini ses cartes
    while len(donneur)!=0 and len(humain)!=0:
        #Lance le tour de Robot si tour=0
        if tour==0:
            print("Mon tour.")
            #Pour robot, on prend une position au hasard entre 1 et n (le nombres de cartes chez humain)
            position=random.randrange(1,len(humain))
            #On donne cette carte à Robot et on l'elimine chez Humain.
            donneur.append(humain[position-1])
            humain.pop(position-1)
            if position==1:
                print("J'ai pris votre ",position,"ère carte.",sep='')
            else:
                print("J'ai pris votre ",position,"ème carte.",sep='')
            #Elimine les paires chez Robot puis atttend le joueur
            donneur=elimine_paires(donneur)
            attend_le_joueur()
            print(45*"*")
            #A la fin du tour de Robot, tour prend la valeur 1 
            tour=tour+1
        else:
            print("Votre tour.")
            print("Votre main est:")
            affiche_cartes(humain)
            #On demande à l'utilisateur d'entrer une position valide parmis le nombre de cartes de Robot
            position=entrez_position_valide(len(donneur))
            if position==1:
                print("Vous avez demandé ma ",position,"ère carte.",sep='')
            else:
                print("Vous avez demandé ma ",position,"ème carte.",sep='')
            #On donne cette carte à Humain et on l'elimine chez Robot
            humain.append(donneur[position-1])
            print("La voilà. C'est un",donneur[position-1])
            print("Avec",donneur[position-1],"votre main est:")
            donneur.pop(position-1)
            affiche_cartes(humain)
            #On elimine les paires chez Humain et on les affiche, puis on attend le joueur
            humain=elimine_paires(humain)
            print("Après avoir défaussé toutes les paires et mélangé les cartes, votre main est:")
            affiche_cartes(humain)
            attend_le_joueur()
            print(45*"*")
            #A la fin du tour de Humain, tour prend la valeur 0
            tour=tour-1
    #Si c'est Robot qui a fini ses cartes, on affiche que Robot a gagné
    #Sinon, si c'est humain qui a gagné, on affiche que humain a gagné
    if len(donneur)==0:
        print("J'ai terminé toutes mes cartes.\nVous avez perdu! Moi, Robot, j'ai gagné.")
    else:
        print("Vous avez terminé toutes vos cartes.\nFélicitations! Vous avez gagné.")

	 
# programme principale
joue()

