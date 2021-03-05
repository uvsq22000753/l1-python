import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Début de votre code
x = 300
y0 = 300
y1 = 100

canvas.create_line(x,y0, x, y1)
canvas.create_oval(x - 50, y0 + 50, x + 50, y0 -50 )
canvas.create_oval(x - 50, y1 + 50, x  + 50, y1 - 50 )
# Fin de votre code

canvas.pack()
root.mainloop()
