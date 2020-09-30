# Pckg import
import sys
from tkinter import *
import time
import random

#globalna zmienna t
t=0

def set_timer():
    global t
    t = t + int(e1.get())
    return t

def countdown():
    global t
    if t > 0:
        l1.config(text=t)
        t = t-1
        l1.after(1000, countdown)
    elif t == 0:
        print('KONIEC')
        l1.config(text = 'PRZERWA')


root = Tk()
root.title('Pomodoro Countdown Timer')
root.geometry('580x360')
# l0 = Label(root, text='CZAS', font='times 35')
# l0.grid(row=1, column=2, )
l1 = Label(root, font='times 15')
l1.grid(row=1, column=2)

times = StringVar()
e1 = Entry(root, textvariable=times)
e1.grid(row=3, column=2)

b1 = Button(root, text='Ustaw', width=20, command=set_timer)
b1.grid(row=4, column=2, padx=20)

b2 = Button(root, text='Start', width=20, command=countdown)
b2.grid(row=6, column=2, padx=20)

root.mainloop()
