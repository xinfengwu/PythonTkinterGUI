from tkinter import *
import tkinter.colorchooser as cc

def changecolor():
    color=cc.askcolor(title='Select a color')
    hexocolor = color[1]
    window.configure(bg=hexocolor)
window = Tk()
window.title('A colorchooser case')

button = Button(text='Change The Window\'s Background',command=changecolor)
button.pack()

window.mainloop()
