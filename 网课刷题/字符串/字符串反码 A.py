s = input()
for p in s:
    if ord("a") <= ord(p) <= ord("z"):
        print(chr(ord("z") - (ord(p) - ord("a") )), end='')
    elif ord("A") <= ord(p) <= ord("Z"):
        print(chr(ord("Z") - (ord(p) - ord("A") )), end='')
    else:
        print(p, end='')