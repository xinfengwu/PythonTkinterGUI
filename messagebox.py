from tkinter import *
from tkinter import messagebox #import messagebox library

def click():
#     messagebox.showinfo(title="Messagebox",message="You just see a messagebox!")
#     messagebox.showwarning(title="Warning",message="You have a Virus!!!")
#     messagebox.showerror(title='ERROR',message='Something went wrong!!!')
#     messagebox.askokcancel(title="Confirm",message="Are you sure to quit?")
#     answer = messagebox.askquestion(title="Ask question",message="Do you like this?")
#     if(answer=='Yes'):
#         print('You did a thing!')
#     else:
#         print('You canceled a thing!')
# 
    answer= messagebox.askyesnocancel(title='Yes, No or Cancel',message='Do you like code?')
    if(answer==True):
        print('You like to code:)')
    elif(answer==False):
        print('Then why are you watching a video on coding?')
    else:
        print('You have dodged the question ')

window = Tk()
window.title = "A messagebox case"
 
button = Button(window,text="submit",command=click)
button.pack()

window.mainloop()
