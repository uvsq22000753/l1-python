# CORRECTION DE TD 

#ON DECOUPE UN PROGRAMME EN DEUX PARTIES 
#1- LES DEFINITIONS DE FONCTIONS 
#2- LE PROGRAMME PRINCIPAL
    #Definitions des variables
    #Appels de fonctions



#1- Créer la fonction qui prend comme argument le temps et renvoie le nombre de seconde total correspondant à ce temps.

def conversion_temps_tuple_en_secondes(temps):
    #temps va etre un tuple de la forme (jour, heure, minute, seconde)
    #Je dois récupérer les secondes , convertir les minutes en secondes et les ajouter
    #Convertir les heures en secondes et les ajouter
    #Convertir les jour en secondes et les ajouter   
    nombre_total_secondes = 0 #Definition de variable
    nombre_total_secondes = temps[3] #cela va sauvegarder la valeur à l'indice 3 de mon tuple temps dans nombre_total_secondes
                                     #A l'indice 3 de mon tuple, cela correspond aux secondes
    #Je veux ajouter les minutes converties en secondes
    #Je récupère mes minutes de mon tuple 
    minutes_en_secondes = temps[2]
    #Je convertis ces minutes en secondes
    minutes_en_secondes = minutes_en_secondes * 60 #Chaque minute est 60 secondes
    #J'ajoute ces secondes aux précédentes
    nombre_total_secondes = nombre_total_secondes + minutes_en_secondes
    #Idem pour heure et les jours
    heures_en_secondes = temps[1] * (60**2)
    jour_en_secondes = temps[0] * (60 ** 2) * 24

    nombre_total_secondes += heures_en_secondes + jour_en_secondes
    return nombre_total_secondes


def conversion_temps_tuple_en_secondes_bis(temps):
    return temps[3] + temps[2] * 60 + temps[1] * (60 ** 2) + temps[0] * (60 ** 2) * 24



def conversion_secondes_en_tuples(secondes):
    #On cherche à savoir combien il y'a de jours possibles dans notre nombres total de secondes
    un_jour = (60 ** 2) * 24 #Nombres de secondes dans un jour
    nombre_de_jour = secondes // un_jour #Le nombre de jour à partir du nombre total de secondes
    #Il faut maintenant mettre à jour notre nombre de secondes restantes
    secondes = secondes - un_jour * nombre_de_jour

    une_heure = 60 ** 2
    nombre_d_heure = secondes // une_heure

    #Mise a jour des secondes restantes
    secondes = secondes - une_heure * nombre_d_heure

    #Idem pour les minutes
    une_minute = 60
    nombre_minutes = secondes // une_minute

    #Mise à jour des secondes 
    secondes = secondes - une_minute * nombre_minutes

    nombre_secondes = secondes

    return (nombre_de_jour,  nombre_d_heure, nombre_minutes , nombre_secondes)
    

def mots_pluriel(mot):
    return str(mot) + "s"


#GENERALEMENT LES FONCTIONS D'AFFICHAGE NE RETOURNE PAS DE VALEUR
def affiche_temps(temps): 
    if (temps[0] > 1): #Si j'ai un nombre de jours supérieur à 2
        print(temps[0], mots_pluriel("jour"), end=" ")
    elif (temps[0] == 1):
        print(temps[0], "jour", end=" ")

    if (temps[1] > 1): #Si j'ai un nombre de jours supérieur à 2
        print(temps[1], mots_pluriel("heure"), end=" ")
    elif (temps[1] == 1):
        print(temps[1], "heure", end=" ")

    if (temps[2] > 1): #Si j'ai un nombre de jours supérieur à 2
        print(temps[2], mots_pluriel("minute"), end=" ")
    elif (temps[2] == 1):
        print(temps[2], "minute", end=" ")

    if (temps[3] > 1): #Si j'ai un nombre de jours supérieur à 2
        print(temps[3], mots_pluriel("seconde"), end=" ")
    elif (temps[3] == 1):
        print(temps[3], "seconde", end=" ")
    pass
             


def utilisateur_tuple():
    nb_jours = int( input("Veuillez entrer un nombre de jour") )
    #ATTENTION : INPUT retourne une chaine de caractère. Il faut la convertir en nombre

    nb_heures = 25
    while (nb_heures > 24 ):
        nb_heures = int(input("Veuillez entrer un nombre d'heures correctes (0 - 24)"))
    
    nb_minutes = 61 
    while (nb_minutes > 60):
        nb_minutes = int(input("Veuillez entrer un nombre de minutes valides (0 - 60)"))
    
    nb_secondes = 61 
    while (nb_secondes > 60):
        nb_secondes = int(input("Veuillez entrer un nombre de secondes valides (0 - 60)"))
    
    return (nb_jours, nb_heures, nb_minutes, nb_secondes)





#PROGRAMME PRINCIPAL :
temps = (0,0,0,59)
secondes = 0  #Definition de la variable secondes
#Convertit un tuples en secondes
secondes = conversion_temps_tuple_en_secondes_bis(temps) #Un appel de fonction (IL nya pas DOuble point pendant les appels de fonctions)
print("Le tuple", temps, "correspond à", secondes, "secondes")
(jour, heure, minute, seconde) = (0, 0, 0, 0) #Definition d'un tuple


(jour, heure, minute, seconde) = conversion_secondes_en_tuples(secondes)
print(secondes, "correspond au tuple", (jour,heure,minute,seconde))
affiche_temps( (jour,heure,minute,seconde) )
print(" ")
print("Saut a la ligne", end=" ")
print("Ligne suivante")


(utilisateur_jour, utilisateur_heure, utilisateur_minute, utilisateur_seconde) = utilisateur_tuple()

temps_bis = (utilisateur_jour, utilisateur_heure, utilisateur_minute, utilisateur_seconde)

affiche_temps(temps_bis)