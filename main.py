from tkinter import *
from tkinter.ttk import *
from time import strftime

top = Tk()
top.title("Digital Clock")


def none():
    text = strftime(" %H,%M,%S %p ")
    label.config(text=text)
    label.after(1000, none)


label = Label(top, font=('digital-7', 50, 'bold'),
              background='black', foreground='yellow')

label.pack(anchor='center')
none()
mainloop()
