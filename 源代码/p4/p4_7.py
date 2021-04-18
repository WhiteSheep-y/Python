# p4_7.py
score = int(input('请输入一个分数：'))

level = 'A' if 100 >= score >= 90 else 'B' if 90 > score >= 80 else 'C' if 80 > score >= 60 else 'D' if 60 > score >= 0 else print('输入错误！')

print(level)
