from tkinter import *

windows = Tk()
windows.title("This is a button case")
photo = PhotoImage(file='favicon.png')
count =0
def click():
    global count
    count +=1
    print(count)
button = Button(windows,
                text='click me',
                command=click,
                font=("Comic Sans",30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound="left"
                )

button.pack()
windows.mainloop()
