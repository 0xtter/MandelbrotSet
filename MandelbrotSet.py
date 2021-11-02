import time
from PIL import Image
from scipy import *
import numpy as np
import math
import os
from tkinter import *
from PIL import Image, ImageDraw, ImageTk
    

Width = 200
Height = 200
Largeur = 3
Centre = (-1,0)
Hauteur = Largeur/(Width/Height)

MAX_ITER = 80

fenetre = Tk()
fenetre.resizable(False, False)
fenetre.title("Ensemble de Mandelbrot")
canvas = Canvas(fenetre, width=Width, height=Height, bg="#ffffff")
canvas.pack(side = "right")

im = Image.new('HSV', (Width, Height), (0, 0, 0))
draw = ImageDraw.Draw(im)

ELargeur = StringVar(fenetre)
EHauteur = StringVar(fenetre)
EZoom = StringVar(fenetre)
EReelle = StringVar(fenetre)
EImaginaire = StringVar(fenetre)
EIteration = StringVar(fenetre)

def mandelbrot(c,z):
    if c == 0 : return 0
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(Height,Width,Centre,Largeur,Hauteur):
    if os.path.isfile("output.png"):os.remove("output.png")
    im = Image.new('HSV', (Width, Height), (0, 0, 0))
    draw = ImageDraw.Draw(im)
    for x in range (0,Width+1):
        for y in range (0,Height+1):
            c = complex(Largeur*(x/Width) - Largeur/2 + Centre[0],Hauteur*(y/Height) - Hauteur/2 - Centre[1])
            m = mandelbrot(c,0)
            hue = int(255 * m / MAX_ITER)
            saturation = 255
            value = 255 if m < MAX_ITER else 0
            draw.point([x, y], (hue, saturation, value))
    im.convert('RGB').save('output.png', 'PNG')

    
def Actualiser():
    global Centre,Largeur,Hauteur,Width,Height,MAX_ITER
    canvas.delete(ALL)
    MAX_ITER = int(EIteration.get())
    Largeur = float(EZoom.get())
    Hauteur = float(EZoom.get())/float(int(ELargeur.get())/int(EHauteur.get()))
    Height = int(EHauteur.get())
    Width = int(ELargeur.get())
    Centre = (float(EReelle.get()),float(EImaginaire.get()))
    canvas.config(width=ELargeur.get(), height=EHauteur.get())
    mandelbrot_set(Height,Width,Centre,Largeur,Hauteur)
    one = PhotoImage(file=r'output.png')
    fenetre.one = one
    canvas.create_image((0,0), image=one, anchor='nw')
    

def ActivePos(event):
    x, y = event.x, event.y
    EReelle.set(Largeur*(x/Width) - Largeur/2 + Centre[0])
    EImaginaire.set(-Hauteur*(y/Height) + Hauteur/2 + Centre[1])
    

    

mandelbrot_set(Height,Width,Centre,Largeur,Hauteur)
image = Image.open("output.png") 
photo = ImageTk.PhotoImage(image)
canvas.create_image(Width/2,Height/2, image=photo)
ELargeur.set(Width)
EHauteur.set(Height)
EZoom.set(Largeur)
EReelle.set(Centre[0])
EImaginaire.set(Centre[1])
EIteration.set(MAX_ITER)

##Entrees
Label(fenetre, text = "Largeur:").pack(side = "top")
Entry(fenetre, width = 10, textvariable = ELargeur).pack(side = "top")
Label(fenetre, text = "Hauteur:").pack(side = "top")
Entry(fenetre, width = 10, textvariable = EHauteur).pack(side = "top")
Label(fenetre, text = "Partie réelle:").pack(side = "top")
Entry(fenetre, width = 10, textvariable = EReelle).pack(side = "top")
Label(fenetre, text = "Partie imaginaire:").pack(side = "top")
Entry(fenetre, width = 10, textvariable = EImaginaire).pack(side = "top")
Label(fenetre, text = "Largeur du zoom:").pack(side = "top")
Entry(fenetre, width = 10, textvariable = EZoom).pack(side = "top")
Label(fenetre, text = "Nombre d'itérations:").pack(side = "top")
Entry(fenetre, width = 10, textvariable = EIteration).pack(side = "top")
    
##Buttons


Button(fenetre, text = "Actualiser", command = Actualiser).pack(side = "top",pady = 20)
canvas.bind("<Button 1>", ActivePos)    

##

fenetre.mainloop()