import tkinter as tk
from tkinter import *

root = Tk()
root.title("Canvas")

canva = tk.Canvas(root, width=400, height=400, bg='black')
canva.pack()

canva.create_line(0, 0, 200, 200, fill='red')
canva.create_rectangle(50, 50, 150, 150, fill='blue')
canva.create_oval(50, 50, 150, 150, fill='green')
canva.create_polygon(200, 100, 200, 100, 100, 200, 0, 100, fill='yellow')

mainloop()