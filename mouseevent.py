from tkinter import *

def doSomething(event):
    print('The mouse event code: ' + str(event.num))
    if(event.num == 1):
        print('The left mouse is clicked')
    elif(event.num ==2):
        print('foo')
    elif(event.num==3):
        print('The right mouse is clicked')
    elif(event.num==4):
        print('The mouse is scrolled up')
    elif(event.num==5):
        print('The mouse is scrolled down')
    print('Mouse coordinates: ' +str(event.x)+ ',' +str(event.y))

window = Tk()
window.title('A mouseevent case')

window.bind('<Button>',doSomething)
# window.bind('<Button-1>',doSomething)# left mouse click
# window.bind('<ButtonRelease>',doSomething)
# window.bind('<Motion>',doSomething)# where the mouse moved
# window.bind('<Leave>',doSomething)#leave the window 
# window.bind('<Enter>',doSomething)#Enter the window 

window.mainloop()
