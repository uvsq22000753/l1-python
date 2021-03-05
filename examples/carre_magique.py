


def affiche_carre(carre):
    for i in range(len(carre)):
        for j in range(len(carre[i])):
            print(carre[i][j], end =" ")
        print("\n")

def test_lignes_egales(carre):
    somme_ligne = [0,0,0,0] 
    for i in range(len(carre)): 
        for j in range(len(carre[i])):
            somme_ligne[i] += carre[i][j]

    val = somme_ligne[0]
    somme_globale = val
    for i in range(1,4):
        if (val != somme_ligne[i]):
            return -1
        somme_globale += somme_ligne[i]
    
    return somme_globale
    
def test_colonnes_egales(carre):
    somme_colonne = [0,0,0,0] 
    for i in range(len(carre)): 
        for j in range(len(carre[i])):
            somme_colonne[i] += carre[j][i]

    val = somme_colonne[0]
    somme_globale = val
    for i in range(1,4):
        if (val != somme_colonne[i]):
            return -1
        somme_globale += somme_colonne[i]
    
    return somme_globale

def test_diagonales(carre):
    somme_diag1 = 0
    somme_diag2 = 0
    
    for i in range(len(carre)): 
        for j in range(len(carre[i])):  
            if (i == j): #Je suis sur la diagonale
                somme_diag1 += carre[i][j]
                print((i,len(carre[j])- 1 - j))
                somme_diag2 += carre[i][len(carre[j])- 1 - j]
    if (somme_diag1 != somme_diag2):
        return -1
    
    return somme_diag1


def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    if (test_lignes_egales(carre) == -1 or test_colonnes_egales(carre) == -1 or test_diagonales == -1):
        return False
    return True

####################################################################################
carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13] ]
carre_pas_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 7, 13] ]

somme_ligne = test_lignes_egales(carre_mag) 
somme_colonne = test_colonnes_egales(carre_mag) 

affiche_carre(carre_mag)

a = estCarreMagique(carre_pas_mag)
if (a == True):
    print("Est carré magique")
else: print("N'est pas carré magique")