# p9_7.py
try:
    f = open('我是一个不存在的文档.txt')
print(f.read())
    sum = 1 + '1'
except:
    print('出错啦')
finally:
    f.close()
