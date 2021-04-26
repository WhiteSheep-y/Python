space=num=cn=en=other=0
s = input()
for c in s:
    if c==' ':
        space+=1
    elif c.isnumeric():
        num+=1
    elif '\u4e00' <= c <= '\u9fef':
        cn+=1
    elif c.isalpha():
        en+=1
    else:
        other+=1
print("您输入的字符串中有：{}个空格，{}个数字，{}个中文字符，{}个英文字符，{}个其他字符。".format(
    space,num,cn,en,other
))
#您输入的字符串中有：1个空格，4个数字，0个中文字符，6个英文字符，1个其他字符。