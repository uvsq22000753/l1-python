import tkinter as tk
from random import *
#Ne pas oublier d'importer tkFont si vous voulez utiliser des polices 
import tkinter.font as tkFont

root = tk.Tk()
#Objet chaîne de caractère contenant une couleur
couleur_utilisateur = tk.StringVar()
#Modification de la chaine de caractère 
couleur_utilisateur.set("blue")

def dessine_cercle_aleatoire():
    a = randint(75, 525)
    b = randint(75, 525)
    canvas.create_oval(a, b, a + 100, b + 100 , fill = couleur_utilisateur.get())
    pass

def dessine_carre_aleatoire():
    a = randint(75, 525)
    b = randint(75, 525)

    canvas.create_rectangle(a, b, a + 100, b + 100 , fill = couleur_utilisateur.get() )
    pass

def choix_couleur():

    #Modification de la variable couleur_utilisateur   
    couleur_utilisateur.set( input("Veuillez choisir une couleur : yellow, green, red, cyan, blue") )   
    pass


#Creation d'une police
my_font1 = tkFont.Font(family='Noto Sans Myanmar', size=36, weight='bold')
my_font2 = tkFont.Font(family='Tahoma', size=15)
my_font3 = tkFont.Font(family='STIXGeneral', size=34, weight='bold')


#Création de mes objets : 1 canvas, 4 boutons
canvas = tk.Canvas(background = "black", borderwidth = "2c", relief = "sunken", height = 300, width = 300)
bouton_carre = tk.Button( text = "Carré", borderwidth = "1c", font = my_font2, highlightbackground = "#501010", highlightcolor = "yellow", overrelief = "sunken", command = dessine_carre_aleatoire)
bouton_cercle = tk.Button( text = "Cercle", borderwidth = "1c", font = my_font1, highlightbackground = "#783794", command = dessine_cercle_aleatoire , activeforeground = "yellow")
bouton_croix = tk.Button( text = "Croix",borderwidth = "1c",  font = 'Waseem', highlightbackground = "#213874", activeforeground = "yellow")
bouton_couleur = tk.Button( text = "Choisir une couleur", borderwidth = "1c", font = my_font3, highlightbackground = "#192929", activeforeground = "yellow", overrelief = "groove", command = choix_couleur)
bouton_undo = tk.Button(text = "Undo",borderwidth = "1c", font = my_font3, highlightbackground = "#192929", activeforeground = "yellow", overrelief = "groove")


#Placement de mes objets sur une grille (GRID)

bouton_carre.grid(row = 1, column = 0)
bouton_cercle.grid(row = 2, column = 0)
bouton_croix.grid(row = 3, column = 0)
bouton_couleur.grid(row = 0, column = 2)
bouton_undo.grid(row = 0, column = 1)
canvas.grid(row = 1, column = 1, rowspan = 3, columnspan = 3)

root.mainloop()