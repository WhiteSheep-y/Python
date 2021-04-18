# p4_13.py
for year in range(2018, 2100):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print(year)
        continue

