n = eval(input())
for a in range(2,n+1):
    for b in range(2,n+1):
        for c in range(b,n+1):
            for d in range(c,n+1):
                if a**3==b**3+c**3+d**3:
                    print("Cube = {},Triple = ({},{},{})".format(a,b,c,d))