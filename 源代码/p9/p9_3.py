# p9_3.py
try:
    f = open('我为什么是一个文档.txt')
    print(f.read())
    f.close()
except OSError:
    print('文件打开的过程中出错啦T_T')
