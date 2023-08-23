
from tkinter import *


def submit():
    print("The temperature is : " +str(scale.get())+ " degrees C")

window = Tk()
window.title("A scale case")

fire_photo =PhotoImage(file="fire_1f525.png")
hot_label = Label(image=fire_photo)
hot_label.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=400,
              orient="vertical", # orientation of scale
              font=('Consolas',20),
              bg="black",
              fg="#00FF00",
              tickinterval=10, # add numeric indicators for value
              showvalue=1, # hide the current value
              resolution=10,
              troughcolor="#00FF00"
              )
scale.pack()


snow_photo =PhotoImage(file="snowflake_2744-fe0f.png")
cold_label = Label(image=snow_photo)
cold_label.pack()

button = Button(window,
                text='submit',
                command=submit)
button.pack()
window.mainloop()
