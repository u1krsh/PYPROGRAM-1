import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
def is_left_click(event):
    label.config(text="Left Click")
def is_right_click(event):
    label.config(text="Right Click")
cvs = tk.Canvas(root,width=300,height=200,bd=20,background="black")
cvs.pack()
label = tk.Label(root,text="")
label.pack()
cvs.bind("<Button-1>",is_left_click)
cvs.bind("<Button-3>",is_right_click)
tk.mainloop()