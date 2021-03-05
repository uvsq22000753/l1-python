import tkinter as tk
from random import * 

CANVAS_HEIGHT = 256
CANVAS_WIDTH = 256

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i, j, color):
    canvas.create_rectangle(i, j, i+2, j+2, fill = color, outline = color)
    


def affiche_pixels_canvas_aléatoire():
    for i in range(0,CANVAS_WIDTH, 2):
        for j in range(CANVAS_HEIGHT, 2):
            color = get_color(i, j, 0)
            draw_pixel(i, j, color)

racine = tk.Tk()

canvas = tk.Canvas(racine, height= CANVAS_HEIGHT, width= CANVAS_WIDTH, bg= "black")
bouton_aléatoire = tk.Button(racine, text= "Aléatoire", font= ('Times', '24'), foreground= "blue", bg= "white", command = affiche_pixels_canvas_aléatoire)
bouton_gris = tk.Button(racine,text= "Dégradé gris", font= ('Times', '24'), foreground= "blue", bg= "white")
bouton_2D = tk.Button(racine, text= "Dégradé 2D", font= ('Times', '24'), foreground= "blue", bg= "white")

bouton_aléatoire.grid(row = 0, column = 0)
bouton_gris.grid(row = 1, column= 0)
bouton_2D.grid(row = 2, column= 0)
canvas.grid(row = 0, column= 1, rowspan= 3)



affiche_pixels_canvas_aléatoire()
racine.mainloop()


