from tkinter import *

def move_up(event):
    canvas.move(myimage,0,-10)

def move_down(event):
    canvas.move(myimage,0,10)

def move_left(event):
    canvas.move(myimage,-10,0)

def move_right(event):
    canvas.move(myimage,10,0)

window = Tk()
window.title('A case of moving images on canvas')

window.bind('<w>',move_up)
window.bind('<s>',move_down)
window.bind('<a>',move_left)
window.bind('<d>',move_right)

canvas = Canvas(window,width=500,height=500)
canvas.pack()

photoImage = PhotoImage(file='img/smile.png')
myimage = canvas.create_image(250,250,image=photoImage,anchor=NW)

window.mainloop()
