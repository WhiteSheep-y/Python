# p17_12.py
from tkinter import *

root = Tk()

# Tkinter总共提供了三种布局组件的方法：pack()，gird()和place()
# grid()方法允许你用表格的形式来管理组件的位置
# row选项代表行，column选项代表列
# 例如 row=1,column=2 表示第二行第三列（0表示第一行）
Label(root, text="作品：").grid(row=0)
Label(root, text="作者：").grid(row=1)

e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)

def show():
    print("作品：《%s》" % e1.get())
    print("作者：%s" % e2.get())
    e1.delete(0, END)
    e2.delete(0, END)

# 如果表格大于组件，那么可以使用sticky选项来设置组件的位置
# 同样你需要使用N，E，S，W以及它们的组合NE，SE，SW，NW来表示方位
Button(root, text="获取信息", width=10, command=show)\
             .grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button(root, text="退出", width=10, command=root.quit)\
             .grid(row=3, column=1, sticky=E, padx=10, pady=5)

mainloop()
