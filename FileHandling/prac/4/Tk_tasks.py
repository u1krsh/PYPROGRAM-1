import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x300")

def add_task():
    task = task_entry.get()
    if not task:
        messagebox.showwarning("Fill a task","No task written")
    else:
        listbox.insert(tk.END,task)
        task_entry.delete(0,tk.END)
def remove_task():
    rem = listbox.curselection()
    if not rem:
        messagebox.showwarning("Not selected","Nothing selected")
    else:
        listbox.delete(rem,tk.END)


tk.Label(text="Enter task: ").pack()
task_entry = tk.Entry(root)
task_entry.pack()
btn_add = tk.Button(text="Add Task",command=add_task)
btn_add.pack()
btn_del = tk.Button(text="Delete Button",command=remove_task)
btn_del.pack()
listbox = tk.Listbox(root,width=300,height=300)
listbox.pack()


tk.mainloop()