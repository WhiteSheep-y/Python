def count_letter(string,char):
    return string.count(char)
string=input()#读入字符串
char=input()#读入字符
print(count_letter(string,char)) #调用count_letter函数统计char在string中出现的次数