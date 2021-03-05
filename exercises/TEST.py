import tkinter as tk
root = tk.Tk()

identifiant = 0
#POINTS cercle
x0 = 0
y0 = 250
x1 = 50
y1 = 300

quantite_deplacement = 50

val_compteur = tk.StringVar()  #VARIABLE DE CONTROLE !!!! 
val_compteur.set("0")

##################################
def initialize_cercle(event):
    global identifiant  #Récupère la variable globale
    identifiant = C.create_oval(x0, y0, x1, y1, fill = "blue")

def avance_cercle():
    global identifiant
    C.move(identifiant, quantite_deplacement,0)

    if (C.coords(identifiant)[2] > 600):
        #ON A PASSE LE BORD DROIT
        C.delete(identifiant)
        identifiant = C.create_oval(x0, y0, x1, y1, fill = "blue")
        #Mettre à jour le compteur
        val_int = int(val_compteur.get())   #On récupère la valeur du compteur avec la methode .get() et on convertit en un entier
        val_int += 1                        #J'ajoute 1 à l'entier
        val_compteur.set(str(val_int))      #Je remodifie la variable val_compteur avec la nouvelle valeur incrémentée
        global identifiant_compteur         #Je recupere l'identifiant de mon objet compteur du Canvas
        C.itemconfig(identifiant_compteur, text = val_compteur.get())   #Je l'argument du compteur dans le canvas avec la nouvelle valeur du compteur.



def recule_cercle():
    global identifiant
    C.move(identifiant, -quantite_deplacement,0)

def reset():
    global identifiant 
    C.delete(identifiant)
    global identifiant_compteur       
    val_compteur.set("0")
    C.itemconfig(identifiant_compteur, text = val_compteur.get() )
    initialize_cercle(0) 



################################## TOUT MES ELEMENTS ########################

C = tk.Canvas( bg = "black", width = 600, height = 600 )
B1 = tk.Button(text ="Avancer", command = avance_cercle)
B2 = tk.Button(text ="Reculer", command = recule_cercle)
B3 = tk.Button(text = "Efface", command = reset)
identifiant_compteur = C.create_text(581, 21, text = val_compteur.get(), fill = "white", width = 20)

#POSITIONNEMENT DANS LA FENETRE PRINCIPALE ROOT
B1.grid(row = 0, column = 0)
B2.grid(row = 0, column = 2)
B3.grid(row = 0, column = 3)
C.grid(row = 1, column = 0, columnspan = 4)


##################################
#Attendre un clic de l'utilisateur dans le canvas : utiliser la méthode bind()
C.bind("<Button-1>", initialize_cercle)

print(C.coords(identifiant))


#################################@
root.mainloop()
