from tkinter import *
import time
import random

window = Tk()
window.title('An animation case')

WIDTH=500
HEIGHT=500

xVelocity =random.randrange(5) 
yVelocity =random.randrange(5) 

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

backgroundImage = PhotoImage(file='img/space.png')
myBackgroundImage = canvas.create_image(0,0,image=backgroundImage,anchor=NW)
photoImage = PhotoImage(file='img/ufo.png')
myImage = canvas.create_image(0,0,image=photoImage,anchor=NW)

while True:
    coordinates = canvas.coords(myImage)
#     print(coordinates)
    if(coordinates[0]>=(WIDTH-photoImage.width()) or coordinates[0]<0):
        xVelocity = -xVelocity
    elif(coordinates[1]>=HEIGHT-photoImage.height()) or coordinates[1]<0:
        yVelocity=-yVelocity
    canvas.move(myImage,xVelocity,yVelocity)
    time.sleep(0.01)
    window.update()
window.mainloop()
