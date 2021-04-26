s = input()
flag=0
for i in s:
    c = chr(ord(i)+1)
    if(ord(c)<=ord('z')):
        print(c,end='')
        flag=1
    else:
        break
if flag:
    print("哈哈，成功遍历！")