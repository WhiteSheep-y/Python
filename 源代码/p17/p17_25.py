# p17_25.py
from tkinter import *

root = Tk()

text = Text(root, width=30, height=10)
text.pack()

text.insert(INSERT, "I love FishC.com!")

photo = PhotoImage(file='fishc.gif')

def show():
    text.image_create(END, image=photo)
    
b1 = Button(text, text="点我点我", command=show)
text.window_create(INSERT, window=b1)

mainloop()
