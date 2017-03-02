import sys
from tkinter import *
import time

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
    clock.after(200, tick)

root = Tk()
time1 = ''

status = Label(root, text="v1.0", bd=1, relief=SUNKEN, anchor=W)
status.grid(row=0, column=0)

clock = Label(root, font=('times', 20, 'bold'), bg='green')
clock.grid(row=0, column=1)

tick()
root.mainloop()