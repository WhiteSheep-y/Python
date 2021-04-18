# p17_16.py
from tkinter import *

root = Tk()

frame = Frame(root)
frame.pack(padx=10, pady=10)

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

def test(content):
    # 注意，这里你不能使用e1.get()或者v1.get()来获取输入的内容
    # 因为validate选项指定为"key"的时候，有任何输入操作都会被拦截到这个函数中
    # 也就是说先拦截，只有这个函数返回True，那么输入的内容才会到变量里边
    # 所以我们要使用%P来获取最新的输入框内容
    if content.isdigit():
        return True
    else:
        return False

testCMD = root.register(test)
Entry(frame, textvariable=v1, width=10, validate="key", \
           validatecommand=(testCMD, '%P')).grid(row=0, column=0)

Label(frame, text="+").grid(row=0, column=1)

Entry(frame, textvariable=v2, width=10, validate="key", \
           validatecommand=(testCMD, '%P')).grid(row=0, column=2)

Label(frame, text="=").grid(row=0, column=3)

Entry(frame, textvariable=v3, width=10, validate="key", \
           validatecommand=(testCMD, '%P')).grid(row=0, column=4)

def calc():
    result = int(v1.get()) + int(v2.get())
    v3.set(result)

Button(frame, text="计算结果", command=calc).grid(row=1, column=2, pady=5)

mainloop()
