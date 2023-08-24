# See more: tkdocs.com/tutorial/menus.html
from tkinter import *
from tkinter import filedialog

def newFile():
    file = filedialog.asksaveasfile(initialdir='',
                                    title='Create a new file',
                                    defaultextension='.txt',
                                    filetypes=[('text files','*.txt'),
                                               ('all files','*.*')
                                              ]
                                    )

def openFile():
    filepath = filedialog.askopenfilename(initialdir='',
                                          title='Open file okay?',
                                          filetypes=(('text files','*.txt'),('all files','*.*')))
    if(filepath):
        file = open(filepath,'r')
        print(file.read())
        file.close()


window = Tk()
window.title('A menubar case')
# Eliminate tear-off menus from menus
window.option_add('*tearOff',FALSE)

testImage = PhotoImage(file='img/smile.png')
openImage = PhotoImage(file='img/open.png')

# Creating a Menubar
menubar = Menu(window)
# window['menu'] = menubar
window.configure(menu=menubar)

# Adding Menus
menu_file = Menu(menubar)
menubar.add_cascade(menu=menu_file,label='File')
menu_edit = Menu(menubar)
menubar.add_cascade(menu=menu_edit,label='Edit')

# Adding Menu Items
# Adding Command Items

menu_file.add_command(label='New',command=newFile,image=testImage,compound='left')
menu_file.add_command(label='Open',command=openFile,image=openImage,compound='left')

# Adding Submenus
menu_export = Menu(menu_file)
menu_file.add_cascade(menu=menu_export,label='Export')
menu_export.add_command(label='PDF')
menu_export.add_command(label='TXT')
menu_export.add_command(label='DOC')

menu_file.add_separator()
menu_file.add_command(label='Exit',command=quit)

window.mainloop()
