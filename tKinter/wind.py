import tkinter as tk
from tkinter import messagebox


def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username == "admin" and password == "admin":
        messagebox.showinfo("Login Status", "Login Successful")
    else:
        messagebox.showerror("Login Status", "Login Failed")
        
window = tk.Tk()
window.title("Login Form")
window.geometry("400x200")

tk.Label(window,text = "Username:").pack(pady=5)
entry_username = tk.Entry(window)
entry_username.pack(pady=5)

tk.Label(window,text = "Password:").pack(pady=5)
entry_password = tk.Entry(window,show="*")
entry_password.pack(pady=5)

btn_login = tk.Button(window,text="Login",command=login)
btn_login.pack(pady=5)

window.mainloop()