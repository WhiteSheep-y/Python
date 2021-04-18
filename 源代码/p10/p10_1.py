# p10_1.py
import easygui as eg
import sys

while 1:
        eg.msgbox("嗨，欢迎进入第一个界面小游戏^_^")

        msg ="请问你希望在鱼C工作室学习到什么知识呢？"
        title = "小游戏互动"
        choices = ["谈恋爱", "编程", "游戏", "琴棋书画"]
        
        choice = eg.choicebox(msg, title, choices)

        # 注意，msgbox的参数是一个字符串
        # 如果用户选择Cancel，该函数返回None
        eg.msgbox("你的选择是: " + str(choice), "结果")

        msg = "你希望重新开始小游戏吗？"
        title = "请选择"

        # 弹出一个Continue/Cancel对话框
        if eg.ccbox(msg, title):
                pass            # 如果用户选择Continue
        else:
                sys.exit(0)     # 如果用户选择Cancel
