from tkinter import *

def move_up(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()-10)

def move_down(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()+10)

def move_left(event):
    label.place(x=label.winfo_x()-10,y=label.winfo_y())

def move_right(event):
    label.place(x=label.winfo_x()+10,y=label.winfo_y())
window = Tk()
window.title('A moving Images case')
window.geometry('500x500')

myImage = PhotoImage(file='img/smile.png')

label = Label(window,image=myImage)
label.place(x=250,y=250)

window.bind('<w>',move_up)
window.bind('<s>',move_down)
window.bind('<a>',move_left)
window.bind('<d>',move_right)

label2 = Label(text='Press w,a,s or d to move the smile',font=('Arial',20)).pack()

window.mainloop()
