# p17_29.py
from tkinter import *

root = Tk()

text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, "I love FishC.com!")

# 将任何格式的索引号统一为元组 (行,列) 的格式输出
def getIndex(text, index):
    return tuple(map(int, str.split(text.index(index), ".")))

start = 1.0
while True:
    pos = text.search("o", start, stopindex=END)
    if not pos:
        break
    print("找到啦，位置是：", getIndex(text, pos))
    start = pos + "+1c"  # 将 start 指向下一个字符

mainloop()
