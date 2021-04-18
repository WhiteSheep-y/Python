import xlrd
wb = xlrd.open_workbook(r'G:\得才教育\合并课表.xls')

flagO = flagE = False
star = end = -1
def RE(s):#正则分析函数
    if s.find('双')!=-1 :
        global flagO 
        flagO = True
    elif s.find('单')!=-1 :
        global flagE
        flagE = True
    else:
        global star,end
        newS = s.split(sep='\n')#将课程信息分割
        week = newS[3].strip('[周]')#取出课程时间范围，并除去无关文字
        week = week.split('-')#以此符号分割字符串
        if(week[0].find(',')!=-1):#特殊处理老师缺课情况
            week[0] = 1
        if len(week)==1:#特殊处理老师代课情况
            week[0]=1
            week.append(17)
        star = int(week[0])
        end = int(week[1])

freeTable = [[[True for i in range(1,6)]for j in range(1,6)]for k in range(1,19)]
for sheetNo in range(wb.nsheets): #遍历表
    sheet=wb.sheet_by_index(sheetNo)
    #sheet = wb.sheet_by_index(2) 
    for c in range(1,6):
        for r in range(3,8):
            cla = sheet.row_values(r)
            if cla[c]!=' ':
                flagO = flagE = False
                RE(cla[c])#传入课程信息
                if flagE:#如果是单周课
                    for k in range(1,18,2):
                        freeTable[k][c-1][r-3]=False
                elif flagO:#如果是双周课
                    for k in range(2,18,2):
                        freeTable[k][c-1][r-3]=False
                else :
                    for k in range(star,end+1):
                        freeTable[k][c-1][r-3]=False
dict = {0:"第一二节",1:"第三四节",2:"第五六节",3:"第七八节",4:"第九十节"}
n = int(input("请输入当前周数："))
#print(freeTable[n])
for i in range(5):
    for j in range(5):
        if j!=2 and freeTable[n][i][j]:
            print("本周周{}{}都没课".format(i+1,dict[j]))