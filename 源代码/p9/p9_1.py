# p9_1.py
file_name = input('请输入要打开的文件名：')
f = open(file_name, 'r')
print('文件的内容是：')

for each_line in f:
    print(each_line)
