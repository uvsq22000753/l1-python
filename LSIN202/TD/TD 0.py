# Exercice 1

#def conversionBase2(nombre):
    #if (nombre == 0):
     #   return[0]
    #res = []
    #while (nombre > 0):
    #    res.append(nombre % 2)
     #   nombre = nombre // 2
    #res.reverse()
    #return res

#conversionBase2(115)

# Exercice 3

def conversionBase(nombre,b):
    if (nombre == 0):
        res = [0]
    res = []
    while (nombre > 0):
        res.append(nombre % b)
        nombre = nombre // b
    res.reverse()
    return res

# Exercice 4

def afficheBaseHexa(liste):
    for i in liste:
        if (i < 10):
            print(i, end= "")
        if ( i == 10):
            print("A", end="")
        if ( i == 11):
            print("B", end="")
        if ( i == 12):
            print("C", end="")
        if ( i == 13):
            print("D", end="")
        if ( i == 14):
            print("E", end="")
        if ( i == 15):
            print("F", end="")


# Exercice 7

def conversionEntier(liste,b):
    res = 0
    puissanceMax = len(liste) - 1
    for i in liste:
        liste[i] * b**(puissanceMax - i)
    return res

# Exercice 9

def etendreEcriture(l,n):
    res = []
    ctrl = n-len(l)
    
    res = [0]*ctrl

    res.extend(l)
    return res

# Exercice 10

def addition(l1,l2,b):
    res = []
    retenu = 0

    if (len(l1) < len(l2)):
        l1 = etendreEcriture(l1, len(l2))
    elif (len(l2) < len(l1)):
        l2 = etendreEcriture(l2, len(l1))
    
    for i in range(len(l1)):
        somme = l1[len(l1) -i -1] + l2[len(l2) -i -1] + retenu
        retenu = 0
        if (somme < b):
            res.insert(0, somme)
        else:
            res.insert(0, somme-b)
            retenu = 1    
    if retenu == 1:
        res.insert(0,retenu)
    return res

test1 = conversionBase(7,2)
test2 = conversionBase(7,2)

print(addition(test1,test2,2))