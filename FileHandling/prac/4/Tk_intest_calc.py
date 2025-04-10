import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x300")

def simple_intrest():
    P = float(prince_entry.get())
    R = float(interest_entry.get())
    T = int(year_entry.get())
    SI = float( (P*R*T)/100)
    tk.messagebox.showinfo("Simple Intrest",SI)

tk.Label(root, text="Enter Principle amount:").pack()
prince_entry = tk.Entry(root)
prince_entry.pack()

tk.Label(root, text="Enter Rate of interest rate:").pack()
interest_entry = tk.Entry(root)
interest_entry.pack()
tk.Label(root, text="Enter Time in years:").pack()
year_entry = tk.Entry(root)
year_entry.pack()

btn = tk.Button(root,text="Calculate SI",command=simple_intrest)
btn.pack()
tk.mainloop()