# p14_6.py
import urllib.request
import re
import os

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')

    return html

def get_img(html):
    p = r'<img class="BDE_Image".*?src="([^"]*\.jpg)".*?>'
    imglist = re.findall(p, html)

    try:
        os.mkdir("NewPics")
    except FileExistsError:
        # 如果该文件夹已存在则覆盖保存！
        pass

    os.chdir("NewPics")

    for each in imglist:
        filename = each.split("/")[-1]
        urllib.request.urlretrieve(each, filename, None)

if __name__ == '__main__':    
    url = "http://tieba.baidu.com/p/3823765471"
    get_img(open_url(url))
