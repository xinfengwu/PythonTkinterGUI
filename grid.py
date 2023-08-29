from tkinter import *

window = Tk()
window.title('A grid case')

titileLabel = Label(window,text='Please Enter Your Info').grid(row=0,column=0,columnspan=2)
firstNameLabel = Label(window,text='First Name',bg='yellow',width=20).grid(row=1,column=1)
lastNameLabel = Label(window,text='Last Name',bg='green').grid(row=2,column=1)
emailLabel = Label(window,text='Email',bg='blue').grid(row=3,column=1)

firstNameEntry = Entry(window).grid(row=1,column=2)
lastNameEntry = Entry(window).grid(row=2,column=2)
emailNameEntry = Entry(window).grid(row=3,column=2)

button = Button(text='Submit').grid(row=4,column=2,columnspan=2)

window.mainloop()
