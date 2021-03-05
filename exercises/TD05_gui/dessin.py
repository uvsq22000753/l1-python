import tkinter as tk  
from random import *

objets = []

def choix_couleur():
    global c 
    c = input("choisir une couleur")
  


def dessine_cerle_alea():
    a = randint(50, 300)
    b = randint(300, 600)
    canvas.create_oval(a, b, a + 100, b + 100, fill= "blue" )

def dessine_carre_alea():
    a = randint(50, 300)
    b = randint(300, 600)
    canvas.create_rectangle(a, b, a + 100, b + 100, fill= c )

def Undo():
    if (len(objets) != 0):
        canvas.delete(objets.pop(-1))




racine = tk.Tk()
racine.title("Mon dessin")
canvas = tk.Canvas(racine, bg= "black", borderwidth="30", height = "600", width= "600")
bouton1 = tk.Button(racine, text="Choisir une couleur", font= ("helvetica","15"), command = choix_couleur)
bouton2 = tk.Button(racine, text="Cercle", font= ("helvetica","15"), command = dessine_cerle_alea)
bouton3 = tk.Button(racine, text="Carré", font= ("helvetica","15"), command = dessine_carre_alea)
bouton4 = tk.Button(racine, text="croix", font= ("helvetica","15"))
undo = tk.Button(racine, text="Undo", font=("helvetica","15"), command= Undo)

bouton1.grid(row=0, column=1)
bouton2.grid(row=1, column=0)
bouton3.grid(row=2, column=0)
bouton4.grid(row=3, column=0)
undo.grid(row=0, column=2)
canvas.grid(row=1, column=1, rowspan = 3, columnspan = 2)

racine.mainloop()