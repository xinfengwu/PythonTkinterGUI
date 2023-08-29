from tkinter import *
from tkinter import ttk

window = Tk()
window.title("A tab case")

notebook = ttk.Notebook(window) # widget that manages a collection of windows/displays

tab1 = Frame(notebook)# new frame for tab 1
notebook.add(tab1,text='Tab 1')
tab2 = Frame(notebook)# new frame for tab 2
notebook.add(tab2,text='Tab 2')
Label(tab1,text='Hello, this is tab#1',width=50,height=25).pack()
Label(tab2,text='Hello, this is tab#2',width=50,height=25).pack()

notebook.pack(expand=True,fill='both')# expand = expand to fill any space not otherwise
                                      # fill = fill space on x and y axis

window.mainloop()
