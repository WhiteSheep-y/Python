# p6_2.py
def discount(price, rate):
    final_price = price * rate
    return final_price

old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣率：'))
new_price = discount(old_price, rate)

print('打折后价格是：', new_price)
print('试图在函数外部访问局部变量final_price的值：%.2f' % final_price)
