ls= input().split()
try:
    a = int(ls[0])
    if a < 0:
        a = '?'
except:
    a = '?'
try:
    b = int(ls[1])
    if b < 0:
        b = '?'
except:
    b = '?'
if a == '?' or b == '?':
    print('{} + {} = {}'.format(a, b, '?'))
else:
    print('{} + {} = {}'.format(a,b,a+b))