#115 / 2 = 57 + 1
#57 / 2 = 28 + 1
#28 / 2 = 14 + 0
#14 / 2 = 7 + 0
#7 / 2 = 3 + 1
#3 / 2 = 1 + 1
#1 / 2 = 0 + 1

# Exercice 1

def conversionBase2(nombre):
    if (nombre == 0):
        return[0]
    res = []
    while (nombre > 0):
        res.append(nombre % 2)
        nombre = nombre // 2
    res.reverse()
    return res

conversionBase2(115)
print(conversionBase2(115))

# Exercice 2

def afficheBase(liste):
    for i in range(len(liste)):
        print([i], end= "")

def afficheBase2(liste):
    for i in liste:
        print(i, end= "")

afficheBase(conversionBase2(115))
afficheBase2(conversionBase2(115))

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

conversionBase(115,2)

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
    
            
afficheBaseHexa(conversionBase(8888,16))

# Exercice 5 : Quelles sont les nombres entiers qu'on peut écrire avec n chiffres en base b?
# n = 5
# b = 2
# 10000 = 2^4
# 11111

# Soit k un nombre à n digits:
#   b^{n-1} < k < b^{n}-1

# Exercice 6 : Donner la valeur de (1001101)2

nombreEntier = 1*2**0 + 0*2**1 + 1*2**2 + 1*2**3 + 0*2**4 + 0*2**5 + 1*2**6
print(nombreEntier)

# Exercice 7

def conversionEntier(liste,b):
    res = 0
    puissanceMax = len(liste) - 1
    for i in liste:
        liste[i] * b**(puissanceMax - i)
    return res

test = conversionBase(115,2)
conversionEntier(test,2)

# Exercice 8 : Additioner (10001101) 2 et (10111001) à la main.
# r:  111  1 
#   10001101 
# + 10111001 
# = 01000110

# base = 5
# r:1
#   4130
#  +2114
# =11244

# Exercice 9

def etendreEcriture(l,n):
    res = []
    ctrl = n-len(1)
    
    res = [0]*ctrl

    res.extend(l)
    return res

base = 8
test = [1, 0, 3, 7]
etendreEcriture(test,10)