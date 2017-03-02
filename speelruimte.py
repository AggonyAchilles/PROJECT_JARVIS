#Test environment
#Test environment
from tkinter import *
import tkinter.messagebox

def doNothing(*args, status):
    status.config(text = "Lol")


root = Tk()

# * MessageBoxes *
tkinter.messagebox.showinfo('Window Title', 'Monkeys can live up to 300 years')
anwser = tkinter.messagebox.askquestion('Question 1', "Are you a faggot?")


if anwser ==  "yes":
    print(":(")


# * Main menu * #

menu = Menu(root, tearoff = False)
root.config(menu = menu)

subMenu = Menu(menu, tearoff = False)

menu.add_cascade(label = "File", menu = subMenu)

subMenu.add_command(label = "New project", command = doNothing)

subMenu.add_command(label = "New...", command = doNothing)

subMenu.add_separator()

subMenu.add_command(label = "Exit", command = root.destroy)

editMenu = Menu(menu, tearoff = False)

menu.add_cascade(label = "Edit", menu = editMenu)

editMenu.add_command(label = "Redo", command = doNothing)

# * Toolbar * #

toolbar = Frame(root, bg = "blue")

insertButt = Button(toolbar,
                    text = "Insert image",
                    command = doNothing).pack(side = LEFT, padx = 2, pady = 2)

printButt = Button(toolbar,
                   text = "Print",
                   command = doNothing).pack(side = LEFT, padx = 2, pady = 2)

toolbar.pack(side = TOP, fill = X)

status = Label(root, text = "Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W).pack(side=BOTTOM, fill=X)


root.mainloop()