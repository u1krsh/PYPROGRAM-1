import tkinter as tk
from tkinter import messagebox, StringVar

root = tk.Tk()
root.geometry("500x500")

canvas = tk.Canvas(width=500,height=400,background="wheat")
canvas.pack()

rad_var = StringVar(value = "circle")
tk.Radiobutton(root,text="Circle",variable=rad_var,value="circle",font=("SF Pro Rounded",10)).pack()

tk.Radiobutton(root,text="Rectangle",variable=rad_var,value="rect",font=("SF Pro Rounded",10)).pack()
tk.Radiobutton(root,text="Line",variable=rad_var,value="line",font=("SF Pro Rounded",10)).pack()

def draw_shap(event):
    wtd = rad_var.get()
    if wtd == "circle":
        canvas.create_oval(30, 30, event.x, event.y, fill="red")  # Bigger visible circle
    elif wtd == "rect":
        canvas.create_rectangle(50, 50, event.x, event.y, fill="blue")
    else :
        canvas.create_line(50, 50, event.x, event.y, fill="green", width=3)


# tk.Button(root, text="Draw Shape", command=draw_shap, font=("SF Pro Rounded", 10)).pack(pady=10)
canvas.bind("<Button-1>",draw_shap)

tk.mainloop()