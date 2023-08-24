from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir='',
                                    title='Save file okay?',
                                    defaultextension='.txt',
                                    filetypes=[('text files','*.txt'),
                                               ('all files','*.*')
                                              ]
                                    )
    filetext = str(text.get(1.0,END))
#     filetext = input('Enter some text I guess: ')
    file.write(filetext)
    file.close()

window = Tk()
window.title('A filedialogsaveas case')

text = Text()
text.pack()

button = Button(text='Save',command=saveFile)
button.pack()

window.mainloop()
