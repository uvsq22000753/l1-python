import tkinter as tk

CANVAS_HEIGHT = 600
CANVAS_WIDTH = 600

val_compteur = tk.StringVar()
val_compteur.set("0")


def clique_cercle(event):
    global balle1
    balle1 = canvas.create_oval(150, 150, 50, 50, fill = "blue")
    

def avance_cercle():
    global balle1
    canvas.move(balle1, 50, 0)
    
    if (canvas.coords(balle1)[2] > 600):
        canvas.delete(balle1)
        balle1 = canvas.create_oval(150, 150, 50, 50, fill = "blue")

        val_int = int(val_compteur.get())
        val_int += 1
        val_compteur.set(str(val_int))



racine = tk.Tk()
canvas = tk.Canvas(racine, bg = "black", height = CANVAS_HEIGHT, width = CANVAS_WIDTH)
Bouton1 = tk.Button(racine, text= "A", font= "helvetica", command = avance_cercle)
Bouton2 = tk.Button(racine, text= "R", font="helvetica", command = recule_cercle)
compteur = canvas.create_text(550, 20, text= val_compteur.get(), fill = "white", width = 20)

Bouton1.grid(row = 0, column = 1)
Bouton2.grid(row = 0, column = 2)
canvas. grid(row = 1, column = 0, columnspan = 4)


canvas.bind("<Button-1>", clique_cercle)

canvas.coords
racine.mainloop()