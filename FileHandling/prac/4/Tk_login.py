import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def login():
    username = entry_username.get()
    password = entry_pass.get()

    if username == "admin" and password== "pass@123":
        tk.messagebox.showinfo("Login status","Login Successful")
    else:
        tk.messagebox.showinfo("Login status","Login Failed")

root.geometry("300x300")

username_label = tk.Label(root,text="Username")
username_label.grid(row = 0, column=0)
entry_username = tk.Entry(root)
entry_username.grid(row = 0, column=1)

pass_label = tk.Label(root,text="Password")
pass_label.grid(row = 1, column=0)
entry_pass = tk.Entry(root)
entry_pass.grid(row= 1, column=1)

btn = tk.Button(root,text="Login",command=login)
btn.grid(row= 3, column= 0)
btn2 = tk.Button(root,text= "Close", command=root.destroy,background="red")
btn2.grid(row = 3, column= 2)
tk.mainloop()