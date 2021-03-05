import tkinter as tk
from random import * 

CANVAS_HEIGHT = 600
CANVAS_WIDTH = 600

x0 = 200
y0 = 200
x1 = 200
y1 = 200

nb_deplacement = 100

def deplacement_ligne(event):
    global bouger
    ligne1 = canvas.create_line(x0, 0, x0, y0 + 400, fill = "red")
    bouger = canvas.move(ligne1, x0 + 100, 0)

def reinitialiser():
    global bouger
    canvas.delete(bouger)

racine = tk.Tk()
canvas = tk.Canvas(bg = "black", height = CANVAS_HEIGHT, width = CANVAS_WIDTH)
recommencer= tk.Button(text = "Recommencer", command = reinitialiser)

ligne1 = canvas.create_line(x0, 0, x0, y0 + 400, fill = "red")
ligne2 = canvas.create_line(600 - x0, 0, 600 - x0, y0 + 400, fill = "yellow")

recommencer.grid(row = 1, column = 0)
canvas.grid(row = 1, column = 1, rowspan = 1)

canvas.bind("<Button-1>", deplacement_ligne)

racine.mainloop()