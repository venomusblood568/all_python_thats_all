from  tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("clock")

def time():
    string = strftime('%H:%M:%S %p')     #if you want to convert this clock in 12 hours('%i:%M:%S %p')
    label.config(text = string)
    label.after(1000, time)


label = Label(root, font=("ds-digital",80 ), background= "red",foreground="red" ) 
label.pack(anchor = "center")
time()

mainloop()


