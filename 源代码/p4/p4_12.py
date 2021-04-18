# p4_12.py
for year in range(2018, 2401):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        break

print("2018年以后出现的第一个闰年是", year)
    
