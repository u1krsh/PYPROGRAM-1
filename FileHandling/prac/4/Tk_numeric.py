import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x300")
def is_num():
    en = entry.get()
    if en.isnumeric():
        messagebox.showinfo("Numeric","It is numeric")
        entry.delete(0,tk.END)
    else:
        messagebox.showerror("Error","It is not a number")
        entry.delete(0,tk.END)
entr = tk.Label(root,text="Enter Number: ")
entr.pack()
entry = tk.Entry(root)
entry.pack()
btn = tk.Button(text="Click",command=is_num)

btn.pack()
root.mainloop()