import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.geometry("300x300")

def cel_to_far():
    cel = float(cel_entry.get())
    far = ((cel * 9/5) + 32)
    messagebox.showinfo("Celsius to Fahrenheit",far)

def far_to_cel():
    far = float(far_entry.get())
    cel= (far - 32) * 5/9
    messagebox.showinfo("Fahrenheit to Celsius",cel)


cel_label = tk.Label(root,text="Enter temp in Celsius: ")
cel_label.pack()
cel_entry = tk.Entry(root)
cel_entry.pack()


far_label = tk.Label(root,text="Enter temp in Fahrenheit: ")
far_label.pack()
far_entry = tk.Entry(root)
far_entry.pack()

btn_to_far = tk.Button(root,text="CEL TO FAR",command=cel_to_far)
btn_to_far.pack()
btn_to_cel = tk.Button(root,text="FAR TO CEL",command=far_to_cel)
btn_to_cel.pack()

tk.mainloop()
