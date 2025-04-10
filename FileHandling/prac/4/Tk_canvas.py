import tkinter as tk
def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x+2, y+2, fill="white")
root = tk.Tk()
root.title("Canvas Drawing")
canvas = tk.Canvas(root, width=400, height=300, bg="black")
canvas.pack()
canvas.bind("<B1-Motion>", draw)
root.mainloop()