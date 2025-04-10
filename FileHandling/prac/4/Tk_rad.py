import tkinter as tk

root = tk.Tk()
root.geometry("300x300")

def change_color():
    color = color_var.get()
    root.config(bg=color)

color_var = tk.StringVar(value="white")

colors = ["Red","Green","Blue"]
for color in colors:
    tk.Radiobutton(root,text=color,value=color.lower(),variable=color_var,command=change_color).pack()
tk.mainloop()



