# p17_18.py
from tkinter import *

root = Tk()

# 创建一个空列表
theLB = Listbox(root, setgrid=True)
theLB.pack()

# 往列表里添加数据
for item in range(11):
    theLB.insert(END, item)

mainloop()
