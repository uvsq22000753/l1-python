def affiche_carre(carre):
    for i in range(len(carre)):
        for j in range(len(carre[i])):
            print(carre[i][j], end="")
        print("\n")

def test_lignes_egal(carre):
    somme_ligne = [0, 0, 0, 0]
    for i in range(len(carre)):
        for j in range(len(carre[i])):
            somme_ligne[i] += carre[i][j]
    
    val = somme_ligne[0]
    somme_global = val
    for i in range(1, 4):
        if (val != somme_ligne[i]):
            return -1
        somme_global += somme_ligne[i]
    
    return somme_global

def test_colonne_egal(carre):
    somme_colonne = [0, 0, 0, 0]
    for i in range(len(carre)):
        for j in range(len(carre[i])):
            somme_colonne[i] += carre[j][i]
    
    val = somme_colonne[0]
    somme_global = val
    for i in range(1, 4):
        if (val != somme_colonne[i]):
            return -1
        somme_global += somme_colonne[i]
    
    return somme_global

def test_diagonal(carre):
    somme_diag1 = 0
    somme_diag2 = 0 
    for i in range(len(carre)):
        for j in range(len(carre[i])):
            if (i == j):
                somme_diag1 += carre[i][j]
                print((i,j))
                somme_diag2 += carre[i][len(carre[j]) - 1 - j]
    if (somme_diag1 != somme_diag2):
        return -1

    return somme_diag1

def estCarreMagique(carre):
    if (test_diagonal(carre) == -1 or test_colonne_egal == -1 or test_diagonal == -1):
        return False
    return True

def estNormal(carre):
    n = len(carre)
    n_square = n ** 2
    liste_element = [i for i in range(1, n_square + 1)]

    for i in range(len(carre)):
        for j in range(len(carre[i])):
            if (carre[i][j] in liste_element):
                a = liste_element.index((carre[i][j]))
                liste_element[a] = 0
                print("Carré pas normal")
                return 0
    print("Carré normal")
    return 1



    




carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
carre_pas_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8]], [16, 2, 7, 13]

somme_ligne = test_lignes_egal(carre_mag)
somme_colonne = test_colonne_egal(carre_mag)

affiche_carre(carre_pas_mag)

print(estNormal(carre_mag))

#a = estCarreMagique(carre_mag)
#if (a == True):
    #print("Est carre magique")
#else:
    #print("N'est pas carre magque")