from tkinter import *

# entry widge = textbox that accepts a single line of user input

window = Tk()
window.title("An entry case")
count = 0
def submit():
    global count
    count += 1
    username = entry.get()
    print("Hello,",username,"+",count)

def backspace():
    entry.delete(len(entry.get())-1,END)

def delete():
    entry.delete(0,END)

username_entry = Entry(window,
              font = ("Arial",50),
              fg="#00FF00",
              bg="black")

username_entry.pack(side="left")

password_entry = Entry(window,
              font = ("Arial",50),
              fg="#00FF00",
              bg="black",
              show="*")

password_entry.pack(side="left")

submit_button = Button(window,
                       text="submit",
                       command=submit)
submit_button.pack(side="bottom")


backspace_button = Button(window,
                       text="backspace",
                       command=backspace)
backspace_button.pack(side="bottom")

delete_button = Button(window,
                       text="delete",
                       command=delete)
delete_button.pack(side="bottom")
window.mainloop()
