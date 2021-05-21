# _*_coding:utf-8 _*_

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break 
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break 
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         # 打印报错，不影响程序运行
#         # print("You can't divide by 0!")
#         # 或者忽略报错
#         pass
#     else:
#         print(answer)


file_name = "python/guess.txt"
with open(file_name) as f:
    word = f.read()
    count = word.lower().count("welcome")
    print(count)

    