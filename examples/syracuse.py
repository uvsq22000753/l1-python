from random import *

##################### ZONE DE DEFINITION DES FONCTIONS #########################

def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste_valeurs_successives = [ ]
    while (n != 1):
        if (n % 2 == 0):
            n = n // 2 
        else:
            n = n * 3 + 1
        liste_valeurs_successives.append(n)
    return liste_valeurs_successives

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    a = []
    for i in range(2, n_max):
        a = syracuse(i)
        if (a[-1] == 1):
            print("Pour n = ", i, "Syracuse est TRUE")
        
    pass

def tempsVol(n):
    liste_vol = syracuse(n)
    temps_vol = len(liste_vol)
    return temps_vol

def tempsVol_nmax(n_max):
    liste_temps_vol = [tempsVol(n) for n in range(1,n_max + 1)]
    return liste_temps_vol    

def temps_vol_max(liste_temps_vol):
    max = 0                            
    indice = 0
    for i in range(0, len(liste_temps_vol)): #Parcours de tous les éléments de ma liste des temps de vol
        if (liste_temps_vol[i] > max):
            max = liste_temps_vol[i]
            indice = i
     
    return (indice, max)

def altitude_max():
    altitude_maximale = 0                                       #Variable stocke altitude max (au début elle est à 0) 
    indice = 0                                                  #Indice pour lequel j'ai l'altitude maximale
    for i in range(1,10000):                                    #On va calculer les syracuse pour les 10000 premiers entiers
        liste_altitudes = syracuse(i)                           #Appel à syracuse (Calcul liste des altitudes pour i)
        for j in range(0, len(liste_altitudes)):                #Pour chacune des 10000 listes, on parcours tous leurs éléments
            if(altitude_maximale < liste_altitudes[j]):         #On verifie si il y'a une altitude dans la liste plus grande que celle maximale courante
                altitude_maximale = liste_altitudes[j]          #Si c'est vrai : alors on met à jour l'altitude maximale
                indice = i                                      #On sauvegarde l'entier pour lequel j'ai une altitude maximale
    
    return (indice, altitude_maximale)



###################### ZONE DE PROGRAMME PRINCIPAL ##############################

n_max = 10000
#print(testeConjecture(n_max))
#print("Le temps de vol de", 7, "est", tempsVol(7))
liste_temps_vol = tempsVol_nmax(n_max)

a = altitude_max()
print(a)
