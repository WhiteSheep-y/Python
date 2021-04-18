# p17_23.py
from tkinter import *

root = Tk()

text = Text(root, width=30, height=2)
text.pack()

# INSERT 索引表示插入光标当前的位置
text.insert(INSERT, "I love\n")
text.insert(END, "FishC.com!")

mainloop()
