import tkinter as tk
from tkinter import *

def new_file():
    print("The file was opened")
    
def file_open():
    print("Old file was opened")
def undo():
    lab.pack_forget()
def redo():
    lab.pack(pady=10)
def makeCommandMenu(root):
    # Create a MenuButton
    command_bar = Menubutton(root, text="Commands", underline=0,font=("SF Pro Rounded", 10))
    command_bar.pack(side=LEFT, padx=2)

    # Create a dropdown menu
    command_bar.menu = Menu(command_bar, tearoff=0)
    command_bar.menu.add_command(label="Undo",underline=0, command=undo,font=("SF Pro Rounded", 10))
    command_bar.menu.add_command(label = "Redo",underline=0, command=redo,font=("SF Pro Rounded", 10))
    command_bar.menu.add_command(label="New..", underline=0, command=new_file,font=("SF Pro Rounded", 10))
    command_bar.menu.add_command(label="Open..", underline=0, command=file_open,font=("SF Pro Rounded", 10))
    command_bar.menu.add_separator()  # Corrected separator syntax
    command_bar.menu.add_command(label="Quit", underline=0, background="maroon", activebackground="red",font=("SF Pro Rounded", 10),
                                 foreground="white", command=root.quit)

    command_bar["menu"] = command_bar.menu  # Attach menu to the Menubuttons
    return command_bar

root = Tk()
root.geometry("400x300")  # Set a window size

# Create the menu bar
mbar = Frame(root, relief=RAISED, borderwidth=2)
mbar.pack(fill=X)
mbar.config(bg="black")
lab = Label(root, text="Menu DEMO", bg="black", fg="white", font=("SF Pro Rounded", 30))
lab.pack(pady=10)
command_bar = makeCommandMenu(mbar)

root.mainloop()
