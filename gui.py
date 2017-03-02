#Test environment

from tkinter import *
import tkinter.messagebox
import time





def doNothing():
    var.set("Updated...")


def exitConfiguration():
    anwser = tkinter.messagebox.askquestion("JARVIS", "Do you really want to shut down JARVIS?")

    if anwser == "yes":
        exit()


root = Tk()
root.geometry("500x500")

var = StringVar()
var.set("Statusbar...")

#Sets the canvas of the root

tkinter.messagebox.showinfo('PROJECT_JARVIS', "JARVIS IS A WORK IN PROGRESS")

#*** main menu ***

menu = Menu(root)
root.config(menu = menu)

subMenu = Menu(menu)

menu.add_cascade(label = "JARVIS_COMMANDS", menu = subMenu)
subMenu.add_command(label = "GOOGLE_SOMETHING", command = doNothing)
subMenu.add_command(label = "OPEN_WEBSITE", command = doNothing)
subMenu.add_separator()
subMenu.add_command(label = "PLAY_MUSIC", command = doNothing)
subMenu.add_command(label = "INTERNET_RADIO", command = doNothing)

subMenu2 = Menu(menu)
menu.add_cascade(label = "JARVIS_INFO", menu = subMenu2)
subMenu2.add_command(label = "TIME", command = doNothing)
subMenu2.add_command(label = "DATE", command  = doNothing)
subMenu2.add_separator()
subMenu2.add_command(label = "DATE_AND_TIME", command = doNothing)

label = Label(root, textvariable = var, bd = 1, relief = SUNKEN, anchor = W).pack(side = BOTTOM, fill= X)

exitButton = Button(root, text = "EXIT_JARVIS", command = exitConfiguration)
exitButton.pack(side = TOP)



root.mainloop()