import easygui as eg

file = open("record2.txt")
eg.textbox(msg='文件【record.txt】的内容如下：', title=' ', text=file.read())
