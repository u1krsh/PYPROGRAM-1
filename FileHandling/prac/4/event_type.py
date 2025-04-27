import tkinter as tk

root = tk.Tk()
root.geometry("500x500")

lab = tk.Label(root, text="a", font=("SF Pro Rounded", 15))
lab.pack(pady=20)

def typ(event):
    x = event.char
    y = "" + x
    lab.config(text=y)

root.bind("<KeyPress>", typ)

root.mainloop()
