# p17_4.py
from tkinter import *

root = Tk()

photo = PhotoImage(file=r"image/bg.gif")
theLabel = Label(root,
                 text="学Python\n到FishC",
                 justify=LEFT,
                 image=photo,
                 compound=CENTER,  # 设置文本和图像的混合模式
                 font=("华康少女字体", 20),  # 设置字体和字号
                 fg="white"  # 设置文本颜色
                 )
theLabel.pack()

mainloop()
