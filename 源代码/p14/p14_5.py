# p14_5.py
import requests
import json

def get_hot_comments(res):
    comments_json = json.loads(res.text)
    hot_comments = comments_json['hotComments']
    with open('hot_comments.txt', 'w', encoding='utf-8') as file:
        for each in hot_comments:
            file.write(each['user']['nickname'] + '：\n\n')
            file.write(each['content'] + '\n')
            file.write("---------------------------------------\n")

def get_comments(url):
    # 给它传个 referer 以免服务器疑神疑鬼的@_@
    # 当然，你这有时间的话将headers头部填写完整，那样妥妥会更好一些……
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
        'referer': 'http://music.163.com/'
        }

    params = "EuIF/+GM1OWmp2iaIwbVdYDaqODiubPSBToe5EdNp6LHTLf+aID/dWGU6bHWXS0jD9pPa/oY67TOwiicLygJ+BhMkOX/J1tZMhq45dcUIr6fLuoHOECYrOU6ySwH4CjxxdbW3lpVmksGEdlxbZevVPkTPkwvjNLDZHK238OuNCy0Csma04SXfoVM3iLhaFBT"
    encSecKey = "db26c32e0cd08a11930639deadefda2783c81034be6445ca8f4fbedd346e1f9567375083aeb1a85e6ad6d9ae4532a49752c2169db8bcc04d38a79f9bed7facea42ee23f1b33538c34f82741318d9b4b846663b53b0b808dd0499dccfbc6c61fbf180c6fb24b1c2dd3c2c450ce09917d74be9424dab836fd2e671988ffbc6ae1b"
    data = {
        "params": params,
        "encSecKey": encSecKey
        }

    name_id = url.split('=')[1]
    target_url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token=".format(name_id)

    res = requests.post(target_url, headers=headers, data=data)
    return res

def main():
    url = input("请输入链接地址：")
    res = get_comments(url)
    get_hot_comments(res)

if __name__ == "__main__":
    main()
