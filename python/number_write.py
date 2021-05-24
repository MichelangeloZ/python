# _*_coding:utf-8 _*_

import json
numbers = [1, 3, 5, 7, 9, 11, 13]
filename = "numbers.json"
with open(filename, "w") as f:
    # 函数json.dump() 接受两个实参：要存储的数据以及可用于存储数据的文件对象
    json.dump(numbers, f)


username = input("What's your name? ")
filename = "name.json"
with open(filename, "w") as f:
    json.dump(username, f)
    print("We'll remember you when you come back, " + username + "!")
    