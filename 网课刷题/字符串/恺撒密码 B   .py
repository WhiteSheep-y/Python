s=input()
for c in s:
    if ord('a') <= ord(c) <= ord('z'):
        print(chr(ord('a')+(ord(c)-ord('a')+3)%26),end='')
    elif ord('A') <= ord(c) <= ord('Z'):
        print(chr(ord('A')+(ord(c)-ord('A')+3)%26),end='')
    else:
        print(c,end='')