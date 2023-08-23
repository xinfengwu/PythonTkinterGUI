from tkinter import *

window = Tk()
window.title("Radiobutton case")

flag_Australia = PhotoImage(file="flag-australia_1f1e6-1f1fa.png")
flag_USA = PhotoImage(file="flag-united-states_1f1fa-1f1f8.png")
flag_Canada = PhotoImage(file="flag-canada_1f1e8-1f1e6.png")
flag = [flag_Australia, flag_USA, flag_Canada]

country = ["Australia", "USA", "Canada"]
def select():
    if(x.get()==0):
        print("You selected Australia.")
    elif(x.get()==1):
        print("You selected USA.")
    elif(x.get()==2):
        print("You selected Canada.")
    else:
        print("Huh?")
x = IntVar()
for index in range(len(country)):
    radiobutton = Radiobutton(window,
                            text=country[index],
                            font=("Impact",50),
                            fg="#00FF00",
                            activeforeground="#00FF00",
                            padx=20,
                            variable=x,
                            value=index,
                            image=flag[index],
                            command=select,
                            compound="right")
    radiobutton.pack(side="bottom")

window.mainloop()
