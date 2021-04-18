# p6_4.py
def discount(price, rate):
    final_price = price * rate
    # 下面试图修改全局变量的值
    old_price = 50
    print('在局部变量中修改后old_price的值是：%.2f' % old_price)
    return final_price

old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣率：'))
new_price = discount(old_price, rate)

print('全局变量old_price现在的值是：%.2f' % old_price)
print('打折后价格是：%.2f' % new_price)
