# p14_3.py
import requests

def get_url(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
    res = requests.get(url, headers=headers)

    return res

def main():
    url = input("请输入链接地址：")
    res = get_url(url)

    with open("res.txt", "w", encoding="utf-8") as file:
        file.write(res.text)
    
if __name__ == "__main__":
    main()
