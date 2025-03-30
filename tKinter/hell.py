import tkinter as tk
from tkinter import *

root = Tk()

root.geometry("300x300")

root.title("test")

Checkbutton(root, text="test1", variable=IntVar(),activebackground="red",activeforeground="green",font=("Helvetica",20)).grid(row= 1,sticky=W)
Checkbutton(root, text="test2", variable=IntVar(),activebackground="blue",activeforeground="white",font=("Helvetica",20)).grid(row= 2,sticky=W)
Checkbutton(root, text="test3", variable=IntVar(),activebackground="yellow",activeforeground="black",font=("Helvetica",20)).grid(row= 3,sticky=W)

Radiobutton(root, text="test1", variable=IntVar(),value=1,activebackground="red",activeforeground="green",font=("Helvetica",20)).grid(row= 4,sticky=W)
Radiobutton(root, text="test2", variable=IntVar(),value=2,activebackground="blue",activeforeground="white",font=("Helvetica",20)).grid(row= 5,sticky=W)

Label(root, text="test",bg="red",fg="white",font=("Helvetica",20)).grid(row= 6,sticky=W)
Entry(root, text="test",bg="black",fg="white",font=("Helvetica",20)).grid(row= 6,column=2,sticky=W)

mainloop()