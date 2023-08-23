from tkinter import *

window = Tk()
window.title("clock1")
photo = PhotoImage(file='favicon.png')
label = Label(window,
              text="bro,do you even code?",
              font=('Arial',40,'bold'),
              fg='#00FF00',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack()

window.iconphoto(True,photo)

window.mainloop()
