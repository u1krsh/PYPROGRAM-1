import tkinter as tk
from tkinter import messagebox
def login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Status", "Login Successful")
    else:
        messagebox.showerror("Login Status", "Invalid Credentials")
# Create window
window = tk.Tk()
window.title("Login Form")
window.geometry("300x200")
# Labels
tk.Label(window, text="Username:").pack(pady=5)
entry_username = tk.Entry(window)
entry_username.pack(pady=5)
tk.Label(window, text="Password:").pack(pady=5)
entry_password = tk.Entry(window, show="*")
entry_password.pack(pady=5)
# Login button
btn_login = tk.Button(window, text="Login", command=login)
btn_login.pack(pady=20)
window.mainloop()