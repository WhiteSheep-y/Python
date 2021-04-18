# p9_9.py
try:
    int('abc')
except ValueError as reason:
    print('出错啦：' + str(reason))
else:
    print('没有任何异常！')
