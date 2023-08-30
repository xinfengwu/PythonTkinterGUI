from tkinter import *
from time import *

def update():
    time_string = strftime('%H:%M:%S %P')
    time_label.config(text=time_string)
    day_string = strftime('%A')
    day_label.config(text=day_string)
    date_string = strftime('%d %m %Y')
    date_label.config(text=date_string)

    window.after(1000,update)

window = Tk()
window.title('A clock Program Case')
window.config(bg='black')

time_label = Label(window,font=('Arial',50),fg='#00FF00',bg='black')
time_label.pack()

day_label = Label(window,font=('Chilanka',50),fg='#00FF00',bg='black')
day_label.pack()

date_label = Label(window,font=('Dyuthi',50),fg='#00FF00',bg='black')
date_label.pack()

update()

window.mainloop()
