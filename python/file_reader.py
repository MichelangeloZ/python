# _*_coding:utf-8 _*_

# 逐条读取
with open ("python/pi_digits.txt") as file_object:
    for line in file_object:
        print(line.rstrip())

# 文件路径
file_path = "python/pi_digits.txt"
with open(file_path) as file_object:
    contents = file_object.read()
    print("\n" + contents)


# 创建一个包含文件各行内容的列表
file_path = "python/pi_digits.txt"
with open(file_path) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())


# 使用文件中的内容
file_path = "python/pi_digits.txt"
with open(file_path) as file_object:
    lines = file_object.readlines()
string = ""
for line in lines:
    string += line.rstrip()
    print(string)
    print(len(string))

打印结果
3.1415926535
12
3.1415926535  8979323846
24
3.1415926535  8979323846  2643383279
36


file_path = "python/pi_digits.txt"
with open(file_path) as file_object:
    lines = file_object.readlines()
string = ""
for line in lines:
    string += line.strip()
print(string)
print(len(string))

