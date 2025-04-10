import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
cnt = 0
def click_ckr():
    global cnt
    cnt += 1
    click_prnt.config(text = cnt)

btn = tk.Button(root,text="CLICK ME!",command=click_ckr)
btn.pack(padx=100,pady=100)
click_prnt = tk.Label(root,text="")
click_prnt.pack()
tk.mainloop()