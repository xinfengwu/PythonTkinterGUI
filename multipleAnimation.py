from tkinter import *
import time
from Ball import *
import random

window = Tk()
window.title('Multiple Animations Case')

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,random.randrange(10),random.randrange(10),"white")
tennis_ball = Ball(canvas,20,20,40,random.randrange(10),random.randrange(10),"red")
basket_ball = Ball(canvas,50,50,20,random.randrange(10),random.randrange(10),"blue")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
