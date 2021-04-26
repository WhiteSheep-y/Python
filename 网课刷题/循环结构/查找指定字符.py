c = input()
s = list(reversed(input()))
flag=0
for i in range(len(s)):
    if s[i]==c:
        flag=1
        break
if flag:
    print("index={:>5}".format(len(s)-i-1))
else:
    print("Not Found")