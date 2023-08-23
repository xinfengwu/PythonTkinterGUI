from tkinter import *

window = Tk() # instantiate an instance of a window
window.title("A window case")
window.geometry("420x420")

icon = PhotoImage(file='favicon.png')
window.iconphoto(True,icon)
window.config(background="#5cfcff")

window.mainloop() # place window on computer screen, listen for events
