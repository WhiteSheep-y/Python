# p4_6.py
score = int(input('请输入一个分数：'))

if 100 >= score >= 90:
    level = 'A'
elif 90 > score >= 80:
    level = 'B'
elif 80 > score >= 60:
    level = 'C'
elif 60 > score >= 0:
    level = 'D'
else:
    print('输入错误！')

print(level)
