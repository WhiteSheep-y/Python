# p17_30.py
from tkinter import *

root = Tk()

text = Text(root, width=30, height=5, undo=True)
text.pack()

text.insert(INSERT, "I love FishC")

def show():
    text.edit_undo()

Button(root, text="撤销", command=show).pack()

mainloop()
