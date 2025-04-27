import tkinter as tk
from tkinter import *

root = Tk()
root.geometry("200x200")
first_name =StringVar()
last_name =StringVar()
radio1a = Radiobutton(root, text = "Martin",value = "Martin",variable=first_name).grid(column=1,row=1)
radio1b = Radiobutton(root, text = "Cooper",value= "Cooper",variable=first_name).grid(column=1,row= 2)
radio1c = Radiobutton(root, text = "Ashton",value= "Ashton",variable=first_name).grid(column=1,row= 3)
radio2a = Radiobutton(root, text = "Brown",value = "Brown",variable=last_name).grid(column=2,row=1)
radio2b = Radiobutton(root, text = "Cupric",value= "Cupric",variable=last_name).grid(column=2,row= 2)
radio2c = Radiobutton(root, text = "Hall",value= "Hall",variable=last_name).grid(column=2,row= 3)
mainloop()