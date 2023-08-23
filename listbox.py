from tkinter import *

def submit():
    if(listbox.curselection()):
        print("You have ordered: ")
#     print(listbox.curselection())
#     print(listbox.get(listbox.curselection()))
        selectedFood = []
        for index in listbox.curselection():
            selectedFood.insert(index,listbox.get(index))

        for f in selectedFood:
            print(f)
    else:
        print("Nothing could be submitted!")

def add():
    if(entryBox.get()!=""):

#     listbox.insert(END,entryBox.get()) # add an item on the bottom
        listbox.insert(0,entryBox.get()) # add an item on the top
        listbox.config(height=listbox.size())
    else:
        print("Please enter an item.")

def delete():
#     listbox.delete(listbox.curselection())
    for index in listbox.curselection():
        listbox.delete(index)

    listbox.config(height=listbox.size())


food = ["pizza","pasta","garlic bread","soup","salad"]
window = Tk()
window.title("A listbox case")

listbox = Listbox(window,
                  bg='black',
                  fg='#00FF00',
                  font=("Arial",40),
                  width=30,
                  selectmode='multiple'
                  )

for index in range(len(food)):
    listbox.insert(index,food[index])
listbox.pack()
listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

addButton = Button(window,
                       text="add",
                       command=add
                       )
addButton.pack()

submit_button = Button(window,
                       text="submit",
                       command=submit
                       )
submit_button.pack()

deleteButton = Button(window,
                       text="delete",
                       command=delete
                       )
deleteButton.pack()

window.mainloop()
