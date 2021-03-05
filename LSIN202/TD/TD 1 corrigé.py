import tkinter as tk
import PIL as pil
from PIL import Image
from PIL import ImageTk 
from tkinter import filedialog
from tkinter import simpledialog

HEIGHT = 300
WIDTH = 300
cpt = 0
create = True

def fermer_fenetre():
    racine.destroy()
    
def compteur(event):
    global cpt
    label['text'] = str(cpt)
    cpt = cpt + 1
    
def affiche_couleur(event):
    if (event.widget == canvas):
        label['text'] = "Couleur = Rouge"
    if (event.widget == canvas_noir):
        label['text'] = "Couleur = Noir"
    
def charger(widg):
    global create
    global photo
    global img
    global canvas
    filename = filedialog.askopenfile(mode = 'rb', title = 'choose a file')
    img = pil.Image.open(filename)
    photo = ImageTk.PhotoImage(img)
    print(photo)
    if create:
        canvas = tk.Canvas(widg, width = img.size[1])
        canvas.create_image(0, 0, anchor = tk.NW, image = photo)
        create = False
    else:
        canvas.pack_forget()
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        canvas.create_image(0,0,anchor = tk.NW, image=photo)

def AfficheLabel(txt):
    label2.config(text = txt)

def ChangeBouton2(txt):
    btn2['text'] = txt
racine = tk.Tk()
affi = tk.Tk()
root = tk.Tk()
affi.title("Une jolie image")
racine.title("Rappel du premier Semestre")

label2 = tk.Label(root, text = "Clic sur le bouton")
label = tk.Label(racine, text = str(cpt))
quitter_fenetre = tk.Button(racine, text = "Fermer", fg ="red", command = fermer_fenetre)
bouton = tk.Button(affi, text = "Charger", fg = "red", command = lambda : charger(affi))
canvas = tk.Canvas(racine, height = HEIGHT, width = WIDTH, bg = "red")
canvas_noir = tk.Canvas(racine, height = HEIGHT, width = WIDTH, bg= "black")

svEntry = tk.StringVar()
edit = tk.Entry(root, textvariable = svEntry)
btn1 = tk.Button(root, text = "Bouton1", command = lambda x=1:AfficheLabel("Clic sur le " + str(x)))
btn2 = tk.Button(root, text = "Bouton2", command = lambda x=2:AfficheLabel("Clic sur le "+str(x)))
btn3 = tk.Button(root, text = "Bouton3", command = lambda x=svEntry:AfficheLabel("Texte: "+x.get()))

btn1.grid(row = 2, column = 0)
btn2.grid(row = 2, column = 1)
btn3.grid(row = 2, column = 2)

label.grid(row = 0, column = 0)
label2.grid(row = 0, column = 0)
quitter_fenetre.grid(row = 1, column = 0)
canvas.grid(row= 0, column= 1)
canvas_noir.grid(row = 1, column = 1)

canvas.bind("<Button-1>", compteur)
canvas.bind("<Double-1>", affiche_couleur)
canvas_noir.bind("<Double-1>", affiche_couleur)

racine.mainloop()
affi.mainloop()
root.mainloop()