import tkinter as tk
import PIL as pil
from PIL import Image
from PIL import ImageTk 
from tkinter import filedialog
from tkinter import simpledialog

matVB=[[]]

def nbrCol(matrice):
    return(len(mat[0]))

def nbrLig(matrice):
    return(len(mat))

def saving(matPix, filename):
    toSave=pil.Image.new("RGBA",(nbrCol(matPix),nbrLig(matPix)))
    for i in range(nbrCol(matPix)):
        for j in range(nbrLig(matPix)):
            toSave.putpixel((i,j),matPix[j][i])
    toSave.save(filename)

def rempliVB(matrice):
    for ligne in matrice:
        for j in range(nbrCol(matrice)):
            if j < nbrCol(matrice) // 2:
                ligne[j] = (0, 255, 0, 255)
            else: 
                ligne[j] = (0, 0, 255, 255)

rempliVB(matVB)
saving(matVB, "vertbleu.png")

def loading(filename):
    toLoad=pil.Image.open(filename)
    mat=[[(255,255,255,255)]*toLoad.size[0] for k in range(toLoad.size[1])]
    for i in range(toLoad.size[1]):
        for j in range(toLoad.size[0]):
            mat[i][j]=toLoad.getpixel((j,i))
    return mat

mat=loading("testBMP.bmp")
taille = nbrLig(mat) * nbrCol(mat) * 3

matrice=loading("vertbleu.png")

def ajouteCarreNoir(mat):
    for i in range(nbrLig(mat) // 4, 3 * nbrLig(mat) //4):
        for j in range(nbrCol(mat) //4, 3*nbrLig(mat) // 4):
            mat[i][j] = (0, 0, 0, 255)

ajouteCarreNoir(matrice)
saving(matrice,"vertbleumodif.png")