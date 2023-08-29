from tkinter import *

window = Tk()
window.title('A canvas case')

canvas = Canvas(window,height=500,width=500)

canvas.create_arc(125,125,375,375,outline='yellow',width=2,style=ARC)
canvas.create_arc(125,125,375,375,start=90,outline='blue',width=2,style=ARC)
canvas.create_arc(125,125,375,375,start=180,outline='red',width=2,style=ARC)
canvas.create_arc(125,125,375,375,start=270,outline='blue',width=2,style=ARC)

canvas.create_line(250,0,250,500,fill='black')
canvas.create_line(0,250,500,250,fill='black')

canvas.create_oval(62,62,437,437,fill='')

canvas.create_rectangle(62,62,437,437,fill='',outline='blue')

canvas.create_polygon(45,34,67,100,400,90,200,400,300,450,fill='',outline='red',smooth=1)
canvas.pack()
window.mainloop()
