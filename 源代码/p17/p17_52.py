# p17_52.py
# 捕获点击鼠标的位置
from tkinter import *

root = Tk()

def callback(event):
    print("点击位置：", event.x, event.y)

frame = Frame(root, width=200, height=200)
frame.bind("<Button-1>", callback)
frame.pack()

mainloop()
