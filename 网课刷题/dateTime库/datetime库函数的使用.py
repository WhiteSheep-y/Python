from datetime import datetime
someday=list(map(int,input().split(',')))
someday.reverse()
someday=datetime(someday.pop(), someday.pop(), someday.pop(), someday.pop(), someday.pop())
print("这一天是星期{}。".format(someday.isoweekday()))
print("这一天的UTC时间是{}。".format(someday.isoformat()))
T="AM" if someday.hour<12 else "PM"
print(someday.strftime("这一天是%b月--%d日--%Y年，%I点%M分{}。".format(T)))

'''
y,m,d,h,mint = input().split(",")
day = datetime(eval(y),eval(m),eval(d),eval(h),eval(mint))
print("这一天是星期{}。".format(day.isoweekday()))
print("这一天的UTC时间是{}。".format(day.isoformat()))
print("这一天是{0:%b}月--{0:%d}日--{0:%Y}年，{0:%I}点{0:%M}分{0:%p}。".format(day))
'''