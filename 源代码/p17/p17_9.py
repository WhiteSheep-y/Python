# p17_9.py
from tkinter import *

root = Tk()

LANGS = [
    ("Python", 1),
    ("Perl", 2),
    ("Ruby", 3),
    ("Lua", 4)]

v = IntVar()
v.set(1)

for lang, num in LANGS:
    b = Radiobutton(root, text=lang, variable=v, value=num)
    b.pack(anchor=W)

mainloop()
