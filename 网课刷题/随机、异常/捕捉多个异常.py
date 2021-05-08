try:
    n=input()
    a,b=input().split(',')
    a=int(a)
    b=eval(b)
    print("{}/{} = {:.2f}".format(n[a],b,int(n[a])/b))
except ZeroDivisionError:
    print('除0错误。')
except IndexError:
    print('索引下标超出范围。')
except:
    print('出错了。')
else:
    print('赞！运行正确，没有错误。')