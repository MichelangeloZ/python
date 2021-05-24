# _*_coding:utf-8 _*_
import json
# filename = "numbers.json"
# with open(filename) as f :
#     numbers = json.load(f)
# print(numbers)

# filename = "name.json"
# with open(filename) as f:
#     username = json.load(f)
#     print("Welcome back, " + username + "!")


## 保存和读取用户生成的数据
# filename = "name.json"
# try:
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     username = input("What is your name? ")
#     with open(filename, "w") as f:
#         json.dump(username, f)
#         print("We'll remember you when you come back, " + username + "!")
# else:
#     print("Welcome back, " + username + "!")

def get_stored_name():
    "若存储了用户名，则获取它"
    filename = "name.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_name():
    "若没有存储，则提示用户输入"
    username = input("What is your name?")
    filename = "name.json"
    with open(filename, "w") as f:
        json.dump(username, f)
    return username

def greet_user():
    "问候用户，并判断名字是否正确"
    username_1 = get_stored_name()
    username_2 = get_new_name()
    if username_1:
        if username_1 != username_2:
            print("两次用户名不一致，请重新输入： ")
            get_new_name()
        else:
            print("Welcome back, " + username_1 + "!")
    else:
        print("We'll remember you when you come back, " + username_2 + "!")

greet_user()



