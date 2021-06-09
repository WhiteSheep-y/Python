l=['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
s=input()
for i in range(len(s)):
    if s[i]=='-':
        print('fu',end=" ")
    else:
        if i!=len(s)-1:
            print(l[eval(s[i])],end=' ')
        else:
            print(l[eval(s[i])])