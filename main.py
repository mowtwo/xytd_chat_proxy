import requests
import time

host = "http://gxy.5br.cn"


def login(user, password):
    loginUrl = f"{host}/waplogin.aspx"
    method = "post"
    data = {
        "logname": user,
        "logpass": password,
        "savesid": "0",
        "action": "login",
        "classid": 0,
        "siteid": "1977",
        "sid": "-2-0-0-0-320",
        "backurl": "myfile.aspx?siteid=1977",
        "g": "登 录",
    }
    try:
        res = requests.post(loginUrl, data=data)
        cookies = res.cookies
        if cookies["sidgxy"] == "-2-0-0-0-320":
            raise Exception("账号或密码错误")
        else:
            return requests.utils.dict_from_cookiejar(cookies)
    except Exception as err:
        print(f"err:{err}")


def getLocalTime():
    localtime = time.asctime(time.localtime(time.time()))
    return localtime


def sendMsg(msg, cookies):
    msgUrl = f"{host}/chat/book_list.aspx"
    data = {
        "face": "",
        "content": msg,
        "action": "add",
        "classid": "876",
        "siteid": "1977",
        "sid": cookies["sidgxy"],
        "tonickname": "大家",
        "g": "发 送",
    }
    headers = {"cookie": str(requests.utils.cookiejar_from_dict(cookies))}
    try:
        res = requests.post(msgUrl, headers=headers, data=data)
        return True
    except Exception as err:
        print(f"err:{err}")
        return False


print(f"开始代理网页行为...现在是{getLocalTime()}")
cookies = {}
while True:
    print("为了使用系统请登录")
    user = input("===账号:")
    password = input("===密码:")
    cookies = login(user, password)
    if cookies != None:
        print("登录成功，你现在可以开始发送聊天信息了")
        break
    else:
        print("你可以选择继续登录或者退出")

while True:
    msg = input("Message>>>")
    if msg == ":exit":
        print("退出程序")
        break
    res = sendMsg(msg, cookies)
    if res:
        print("发送成功")
