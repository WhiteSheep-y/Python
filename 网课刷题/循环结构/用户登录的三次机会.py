name = input()
psw = input()
cnt = 0
while name!='Kate' and psw!='666666':
    cnt+=1
    if cnt==3:
        break
    name = input()
    psw = input()
else:
    print('登录成功！')
if cnt>=3:
    print('3次用户名或者密码均有误！退出程序。')