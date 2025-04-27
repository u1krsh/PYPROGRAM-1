import tkinter as tk
from tkinter import messagebox, StringVar
import random
root= tk.Tk()
root.geometry("400x400")
root.config(background="#10131d")
tk.Label(text="🪨",font=("Segoe UI Emoji",75),foreground="wheat",background="#10131d").pack(anchor="center")

rps_var = StringVar(value="rock")
frame = tk.Frame(root)
frame.pack(pady=50)
tk.Radiobutton(text="🪨",variable=rps_var,value="rock",font=("Segoe UI Emoji",35),foreground="wheat",background="#10131d",selectcolor="#10131d").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(text="📃",variable=rps_var,value="paper",font=("Segoe UI Emoji",35),foreground="wheat",background="#10131d",selectcolor="#10131d").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(text="✂️",variable=rps_var,value="sciss",font=("Segoe UI Emoji",35),foreground="wheat",background="#10131d",selectcolor="#10131d").pack(side=tk.LEFT, padx=10)

def play():
    var = rps_var.get()
    sel = ["rock","paper","sciss"]
    x = random.choice(sel)
    if x == "rock" and var == "rock" or x =="paper" and var =="paper" or x=="sciss" and var == "sciss":
        messagebox.showinfo(message="No One Wins")
    elif x == "rock" and var == "sciss" or x == "paper" and var == "rock" or var == "sciss" and x == "paper":
        messagebox.showinfo(message="Computer win")
    else:
        messagebox.showinfo(message="You win")

tk.Button(command=play).pack()
root.mainloop()