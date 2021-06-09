try:
    l=eval(input())
    t={}
    for i in l:
        t[i]=t.get(i,0)+1
    m=max(t.values())
    for i in t:
        if m==t.get(i):
            print(i)
            break
except:
    print('Fail。') 