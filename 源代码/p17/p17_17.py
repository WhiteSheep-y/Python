# p17_17.py
from tkinter import *

root = Tk()

# 创建一个空列表
theLB = Listbox(root, setgrid=True)
theLB.pack()

# 往列表里添加数据
for item in ["钢铁侠", "蜘蛛侠", "绿灯侠", "神奇女侠"]:
    theLB.insert(END, item)

theButton = Button(root, text="删除", command=lambda x=theLB: x.delete(ACTIVE))
theButton.pack()

mainloop()
