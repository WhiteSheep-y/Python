# p17_38.py
from tkinter import *

root = Tk()

def callback():
    print("~被调用了~")

# 创建一个顶级菜单
menubar = Menu(root)
menubar.add_command(label="Hello", command=callback)
menubar.add_command(label="Quit", command=root.quit)

# 显示菜单
root.config(menu=menubar)

mainloop()