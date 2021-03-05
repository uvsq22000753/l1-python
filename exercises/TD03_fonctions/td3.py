#temps_tuple = (1, 2, 3, 4) #la variable temps_tuple est un "tuple"
#temps_liste = [1, 2, 3, 4] #la variable temps_liste est une "liste"

#Quand on définit un tuple, on utilise des parenthèses. Quand on accède à un élément d'un tuple on renseigne l'index (ou indice)
#entre crochets

#Affichage de tous les éléments d'un tuple un par un.
#print(temps_tuple[3]) 

########################### USAGE DES FONCTIONS #######################################
# 1- On définit la fonction : on lui donne donne un nom, ses arguments, et ce qu'elle doit faire.
    #Une fonction commence par le mot clé def. 
    #Une fonction se termine par un mot clé ("pass", "return")

# 2- On peut appeler la fonction par son nom, et ainsi exécuter le code qui se trouve à l'intérieur.

temps =   (3,4, 59, 12)
c = 0

#position: 0, 1, 2, 3 
#Pour définir on utilise le mot clé "def" suivi du nom de la fonction 
def tempsEnSeconde(temps): #Ceci est une définition de fonction
    a = 12
    b = 13
    c = a + b
                                        #Le code de la fonction 
    return c
#Le code d'une fonction n'est pas exécutée tant que la fonction n'est pas "appelée"


# ON NE PEUT PAS APPELER UNE FONCTION AVANT QU'ELLE SOIT DEFINIE : 
#1- DEFINTION FONCTION 
#2- APPEL FONCTION 

c = tempsEnSeconde( (2,3,5,7) )       #APPEL DE FONCTION : Cela va exécuter le code de la fonction définie plus haut 
#print(c)


#Un programme c'est un assemblage de fonctions !!! 
#Une fonction est une tâche particulière.
#Vous pouvez assembler des fonctions, récuperer leur resultats pour construire des programmes plus complexes.

#1 DEFINITION FONCTION
def addition(a,b):
    d = a + b
    return d
    
#2 APPEL DE FONCTION
e = addition(12,31)

#ICI LE CODE EST APRES L APPEL DE FONCTION, SI ON A PAS RECUPERE LA VALEUR DE d QUELQUE PART
#ALORS CETTE VALEUR N EXISTE PLUS DANS LE CODE PAR LA SUITE (UNIQUEMENT DANS LA FONCTION)
#print(e)

#DEFINITION DE LA FONCTION MULTIPLICATION
def test ():
    c = addition (2, 2)                  #Appel de la fonction Addition DANS la fonction multiplication
    resultat = (nombre1 * nombre2) + c  #Sauvegarde multiplication nombre1 * nombre 2 + c dans resultat
    return resultat                     #Retourne la valeur de resultat

#ON EST DANS LE CODE QUI S'EXECUTE (CODE PRINCIPAL)
nombre1 = 1
nombre2 = 2
resultat = (test() + addition(1,2))

#print(resultat)



#On regarde d'abord l'execution de multiplication
    # Il appel la fonction addition avec les arguments 2 et 2
    # On regarde la fonction addition 
        #FONCTION ADDITION
            # Fait l'adition de 2 + 2 et retourne le resultat
            #On sort de la fonction ADDITION
    #On sauvegarde dans c, le resultat de l'addition, c à d : 4
    #La fonction multiplication ensuite calcule nombre1 * nombre2 + 4
    #resultat = (1 * 2) + 4 = 6
    #On retourne LA VALEUR de résultat
#On revient dans le code principale
# Multiplication() vaut 6
# le programme fait ensuite l'addition entre 1 et 2 
    #La fonction addition retourne 3 
#On revient dans le code principal
#On fait l'addition entre Multiplication() et addition(1,2) = 6 + 3 = 9





def multiplication(a,b):
    return a*b

#Si tu as envie par la suite de reutiliser le resultat de cette multiplication il faut imperativement
#le stocker dans une variable.

def multiplication_et_addition(a,b,c,d):
    mult = multiplication(a,b)
    add = addition(c,d)
    return (mult, add)

#Definition de la variable mult_add qui recupere le resultat de la fonction multiplication et addition
mult_add = multiplication_et_addition(1,1,1,1)  #APPEL de la fonction multiplication et addition
print(type(mult_add))
