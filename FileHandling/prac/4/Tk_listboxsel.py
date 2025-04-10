import tkinter as tk

root =tk.Tk()
root.geometry("300x300")
def disp_lbl():
    txt = listbox.get(listbox.curselection())
    show_lbl.config(text=txt)

listbox = tk.Listbox(root,width=300)
fruits = ["apple","banana","watermelon"]
for i in fruits:
    listbox.insert(tk.END,i)
listbox.pack()

show_lbl = tk.Label(root,text="")
show_lbl.pack()
btn = tk.Button(text="Show",command=disp_lbl)
btn.pack()
tk.mainloop()