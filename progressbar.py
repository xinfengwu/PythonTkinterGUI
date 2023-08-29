from tkinter import *   
from tkinter.ttk import *
import time

def start():
    GB = 10
    speed = 1
    download = 0
    bar['value']=0
    while(download<GB):
        time.sleep(0.05)
        bar['value'] += (speed/GB)*100
        download += speed
        text.set(str(download) + '/' + str(GB) + ' GB completed')
        percent.set(str(int((download/GB)*100)) + '% completed')
        window.update_idletasks()

window = Tk()
window.title('A progressbar case')

percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

percentLabel = Label(window,textvariable=percent).pack()
taskLabel = Label(window,textvariable=text).pack()

Button(window,text='Download',command=start).pack()

window.mainloop()
