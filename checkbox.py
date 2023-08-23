from tkinter import *

def check():
    if(x.get()):
        print("You agree!")
    else:
        print("You don't agree!")

window = Tk()
window.title("checkbox case")
x=BooleanVar()
photo=PhotoImage(file='./favicon.png')
check_botton = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           image=photo,
                           compound='left',
                           activebackground="black",
                           activeforeground="#00FF00",
                           fg="#00FF00",
                           font=("Arial",25),
                           bg="black",
                           command=check)
check_botton.pack()

window.mainloop()
