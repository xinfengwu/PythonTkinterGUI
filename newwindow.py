from tkinter import *

def creatWindow():
#     new window 'on top' of other windows,linked to a 'bottom' window
    newWindow = Toplevel()
    newWindow.title('This is a toplevel window')
    Button(newWindow,text='Destroy Old Window',command=destroy).pack()

def destroy():
    window.destroy()

window = Tk()
window.title('A bottom window')

Button(window,text='Create a New Window',command=creatWindow).pack()

window.mainloop()
