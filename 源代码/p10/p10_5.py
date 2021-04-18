# p10_5.py
from easygui import EgStore

# 定义一个叫做“Settings”的类，继承自EgStore类
class Settings(EgStore):

    def __init__(self, filename):  # 需要指定文件名
        # 指定要记住的属性名
        self.author = ""
        self.book = ""
        
        # 必须执行下面两个语句
        self.filename = filename
        self.restore()

# 创建“Settings”的实例化对象“settings”
settingsFilename = "settings.txt"
settings = Settings(settingsFilename)

author = "小甲鱼"
book = "《零基础入门学习Python》"

# 将上面两个变量的值保存到“settings”对象中
settings.author = author
settings.book = book
settings.store()
print("\n保存完毕\n")
