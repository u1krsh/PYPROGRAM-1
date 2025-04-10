import tkinter as tk
from tkinter import messagebox

from bokeh.models import Button

root = tk.Tk()

def add_num():
    a = int(num1_entry.get())
    b = int(num2_entry.get())
    c = a +b
    messagebox.showinfo("Addition Answer",c)
def sub_num():
    a = int(num1_entry.get())
    b = int(num2_entry.get())
    c = a -b
    messagebox.showinfo("Subtraction Answer",c)
def mul_num():
    a = int(num1_entry.get())
    b = int(num2_entry.get())
    c = a *b
    messagebox.showinfo("Multiplication Answer",c)
def div_num():
    a = int(num1_entry.get())
    b = int(num2_entry.get())
    c = a /b
    messagebox.showinfo("Division Answer",c)


root.geometry("300x300")

num1_label = tk.Label(root,text="Number 1 ")
num1_label.grid(row=0,column=0)
num1_entry = tk.Entry(root)
num1_entry.grid(row=0,column=1)

num2_label = tk.Label(root,text="Number 2 ")
num2_label.grid(row=2,column=0)
num2_entry = tk.Entry(root)
num2_entry.grid(row=2,column=1)

btn_add = tk.Button(text="Add",command=add_num)
btn_add.grid(row= 3, column=0)
btn_sub = tk.Button(text="Subtract",command=sub_num)
btn_sub.grid(row= 3, column=1)
btn_mul = tk.Button(text="Multiply",command=mul_num)
btn_mul.grid(row= 4, column=0)
btn_div = tk.Button(text="Divide",command=div_num)
btn_div.grid(row= 4, column=1)
tk.mainloop()
