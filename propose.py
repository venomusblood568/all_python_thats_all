# Python program to create 
# yes/no message box
  
  
from ast import Break
from os import abort
import tkinter as tk
from tkinter import * 
from tkinter import messagebox as mb
  
  
def call():
    res = mb.askquestion('none','so are you ready for your surprise ?')
    root.destroy()  # this line will delete the old window so it will look more clean more than ever!!!!
    if res == 'yes' :
        mb.showwarning("none","are you sure na if you went ahead nothing can be done then !! keep in mind ")   
    else :
        mb.showwarning("none","error",**abort)

       
    if res == "yes":
        mb.showerror("none","do you remember the day when we met for the first time ?")
    
    
    if res == "yes":
        mb.showerror("none","i dont know about you but i dont remember but you know what you have became of the my daily stuff and without you it feels incomplete so!!!!")


    if res == "yes":
        mb.askquestion("none","so i wanted to ask you something that has been bothring me for a while now so can i ask ? ")
    else:
        mb.showerror('none','its ok 🙂')

    if res == "yes":
        mb.askquestion("none","so my favourite human i was asking that valentine day is gone now i know but will you be my lifetime valentine ??")

    if res =="yes":
        mb.showinfo("none","I LOVE YOU!!!")
        root.destroy()
    else:
        root.destroy()
    
    root.destroy()    



# Driver's code
root = tk.Tk()
canvas = tk.Canvas(root, 
                   width = 200, 
                   height = 200)
  
canvas.pack()
b = Button(root,
           text ='hey girl click me!!',
           command = call)
  
canvas.create_window(100, 100, 
                     window = b)



    

 
root.mainloop()
