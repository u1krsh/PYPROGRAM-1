from tkinter import *

def new_file():

    writ = Text(root, bg="black", fg="white", font=("SF Pro Rounded", 14))
    writ.pack(pady=10)
    with open("file.txt", "r") as f:
        writ.insert("1.0", f.read())

def file_open():
    print("Old file was opened")

def undo():
    lab.pack_forget()

def redo():
    lab.pack(pady=10)

def makeCommandMenu(root1):
    # Create a MenuButton
    command_bar = Menubutton(root1, text="Commands", underline=0, font=("SF Pro Rounded", 10))
    command_bar.pack(side=LEFT, padx=2)

    # Create a dropdown menu
    command_bar.menu = Menu(command_bar, tearoff=0)
    command_bar.menu.add_command(label="Undo",underline=0, command=undo,font=("SF Pro Rounded", 10))
    command_bar.menu.add_command(label = "Redo",underline=0, command=redo,font=("SF Pro Rounded", 10))
    command_bar.menu.add_command(label="New..", underline=0, command=new_file,font=("SF Pro Rounded", 10))
    command_bar.menu.add_command(label="Open..", underline=0, command=file_open,font=("SF Pro Rounded", 10))
    command_bar.menu.add_separator()  # Corrected separator syntax
    command_bar.menu.add_command(label="Quit", underline=0, background="maroon", activebackground="red", font=("SF Pro Rounded", 10),
                                 foreground="white", command=root1.quit)

    command_bar["menu"] = command_bar.menu  # Attach menu to the Menubuttons
    return command_bar

root = Tk()
root.geometry("400x300")
root.title("Tkinter Menu Demo")
root.configure(bg="black")

lab = Label(root, text="Menu DEMO", bg="black", fg="white", font=("SF Pro Rounded", 30))
lab.pack(pady=10)

makeCommandMenu(root)

root.mainloop()
