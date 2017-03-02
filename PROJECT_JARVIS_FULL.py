#PROJECT_JARVIS_PROGRAM
#Ian Angillis
#Documentation is in a different file
#

#*** Imports ***

try:
    from tkinter import *
except ImportError:
    raise ImportError("The tkinter module is required to run JARVIS")

try:
    import tkinter.messagebox
except ImportError:
    raise ImportError("The tkinter.messagebox module is required to run JARVIS")

try:
    import datetime
except ImportError:
    raise ImportError("The datetime module is required to run JARVIS")

try:
    import os
except ImportError:
    raise ImportError("The os module is required to run JARVIS")

try:
    import webbrowser
except ImportError:
    raise ImportError("The webbrowser module is required to run JARVIS")

try:
    import urllib.request
except ImportError:
    raise ImportError("The urllib.request module is required to run JARVIS")

try:
    import time
except ImportError:
    raise ImportError("The time module is required to run JARVIS")

#*** Global variables ****



#*** JARVISAPP class ****

class Jarvisapp:
    #Sets up JARVIS and the GUI
    def __init__(self, master):

        #*** CREATING THE USER INTERFACE ***

        #Referencing to the master
        self.master = master


        #Creating the first menu
        self.createDropDownMenus(self.master)

        #Creating the toolbar

        #Creating the statusbar
        self.createStatusBar(self.master)
        #Creating dynamic clock and date


    def createDropDownMenus(self, master):
        self.menu = Menu(self.master)
        self.master.config(menu = self.menu)
        self.subMenu_1 = Menu(self.menu)

        self.menu.add_cascade(label="JARVIS COMMANDS", menu = self.subMenu_1)

        self.subMenu_1.add_command(label = "Google something", command = self.googleSomething)


    def googleSomething(self):
        self.statusVariable.set("Ready to google")
        self.entrytext = StringVar()
        Entry(self.master, textvariable=self.entrytext).pack()
        Button(self.master, text = "Google!", command = self.googleIt).pack()



    # Accepts input and changes all the spaces into '+'
    def googleIt(self):
        self.statusVariable.set("Googling!")
        webbrowser.open('http://www.google.be/?gfe_rd=cr&ei=U1-jWNauLYHEXsK_nJAH&gws_rd=ssl#q=' + self.entrytext.get())
        self.statusVariable.set("Ready for the next task")

    def createStatusBar(self, master):
        self.statusVariable = StringVar()
        self.status = Label(self.master, textvariable = self.statusVariable, bd=1, relief=SUNKEN, anchor=W).pack(side=BOTTOM, fill=X)
        self.statusVariable.set("Launching JARVIS")




#*** JARVIS LOOP***

master = Tk()
master.geometry("1280x720")
jarvis = Jarvisapp(master)
master.mainloop()
