#vlozenie modulov
import tkinter
import random
import string
import keyboard

#vytvorenie platna
canvas = tkinter.Canvas(width=500, height=300, background="white")
canvas.pack()

#zadeklarovanie povodnych suradnic
x = random.randint(10,490)
y = 10

#nahodny vyber pismena
pismenko = random.choice(string.ascii_lowercase)

def spawn(): #funkcia na vytvorenie vajicka
    #zadeklarovanie globalnych premennych
    global x,y
    global pismenko

    #zmazanie platna
    canvas.delete("all")

    #vytvorenie vajka a posunu
    canvas.create_oval(x,y,x+15,y+25)
    y += 5

    if y >= 200: #podmienka na vypisanie pismenka
        canvas.create_text(x+7,y+6,text=pismenko,font="Arial 10")
        
    if y <= 300 and keyboard.is_pressed(pismenko): #podmienka na uspesne pokracovanie
        x = random.randint(10,490)
        y = 10
        pismenko = random.choice(string.ascii_lowercase)
    elif y > 300 and not keyboard.is_pressed(pismenko): #podmienka na ukoncenie hry
        canvas.delete("all")
        return canvas.create_text(250,150,text="HAHA POKAZIL/A SI TO!",font="Arial 30")

    #update platna po casovom intervale
    canvas.after(50,spawn)

#vyvolanie funkcie
spawn()
