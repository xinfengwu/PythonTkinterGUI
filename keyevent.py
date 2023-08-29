from tkinter import *

def doSomething(event):
#     print('You pressed ', + str(event.keysym))
#     print(event.keysym)
    prompt.set('You pressed: '+ event.keysym)

window = Tk()
window.title('A key event case')
prompt = StringVar()
label = Label(window,textvariable=prompt,font=('Ubuntu',20))
label.pack()

window.bind('<KeyPress>',doSomething)


window.mainloop()
