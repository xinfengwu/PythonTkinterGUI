from tkinter import *
from tkinter import filedialog
import os

def openfile():
    filepath = filedialog.askopenfilename(initialdir='',
                                          title='Open file okay?',
                                          filetypes=(('text files','*.txt'),('all files','*.*')))
    if(filepath):
        file = open(filepath,'r')
        print(file.read())
        file.close()

window = Tk()
window.title('A filedialog case')

button = Button(text='Open',command=openfile)
button.pack()

window.mainloop()
