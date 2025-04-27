import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x300")
root.config(background="#1a1f30")

tk.Label(root,text="REGISTRATION FORM",font=("SF Pro Rounded", 15),background="#1a1f30", foreground="wheat").place(x=55,y=0)

tk.Label(root,text="Enter Name: ",font=("SF Pro Rounded",10),background="#1a1f30", foreground="wheat").place(y=40,x=5)
nam_ent = tk.Entry(background="#1a1f30", foreground="wheat",font=("SF Pro Rounded",10))
nam_ent.place(x=120,y=40)

tk.Label(root,text="Enter Email: ",font=("SF Pro Rounded",10),background="#1a1f30", foreground="wheat").place(y=80,x=5)
email_ent = tk.Entry(background="#1a1f30", foreground="wheat",font=("SF Pro Rounded",10))
email_ent.place(x=120,y=80)

tk.Label(root,text="Enter Number: ",font=("SF Pro Rounded",10),background="#1a1f30", foreground="wheat").place(y=120,x=5)
num_ent = tk.Entry(background="#1a1f30", foreground="wheat",font=("SF Pro Rounded",10))
num_ent.place(x=120,y=120)

tk.Label(root, text="Gender:", font=("SF Pro Rounded", 10), background="#1a1f30", foreground="wheat").place(x=5, y=160)
gender_var = tk.StringVar(value="male")  # Default value

tk.Radiobutton(root, text="Male", variable=gender_var, value="male", background="#1a1f30", foreground="wheat", selectcolor="#1a1f30", font=("SF Pro Rounded", 10)).place(x=120, y=160)
tk.Radiobutton(root, text="Female", variable=gender_var, value="female", background="#1a1f30", foreground="wheat", selectcolor="#1a1f30", font=("SF Pro Rounded", 10)).place(x=180, y=160)


tk.Label(root, text="Select Country", font=("SF Pro Rounded", 10), background="#1a1f30", foreground="wheat",activebackground="#1a1f30").place(y=200, x=5)
drp_var = tk.StringVar(value="United States")
country_menu = tk.OptionMenu(root, drp_var, "United States", "India", "France")
country_menu.config(background="#1a1f30", foreground="wheat", activebackground="#2a2f40", activeforeground="white",borderwidth=0,highlightthickness=0,relief="flat")
country_menu.place(y=200, x=120)

def disp():
    nam = nam_ent.get()
    mal = email_ent.get()
    num = num_ent.get()
    gen = gender_var.get()
    con = drp_var.get()

    messagebox.showinfo(message=f"Your name is {nam} with e-mail: {mal} number {num} your gender is {gen} and are from {con}")

tk.Button(text="Register",command=disp, font=("SF Pro Rounded", 10), background="#1a1f30", foreground="wheat",activebackground="#1a1f30").place(y=240,x=100)

root.mainloop()