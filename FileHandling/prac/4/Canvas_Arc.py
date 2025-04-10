import tkinter as tk
from tkinter import messagebox
def show_message():
    response = messagebox.askyesno("Confirm", "Do you want to continue?")
    if response:
        label_result.config(text="You clicked Yes!")
    else:
        label_result.config(text="You clicked No!")
root = tk.Tk()
root.title("Messagebox Example")
btn_confirm = tk.Button(root, text="Click Me", command=show_message)
btn_confirm.pack(pady=5)
label_result = tk.Label(root, text="")
label_result.pack(pady=5)
root.mainloop()