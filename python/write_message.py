# _*_coding:utf-8 _*_

filename = "python/program.txt"
with open(filename, "w") as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 附加到文件
# 参'a' ，以便将内容附加到文件末尾，而不是覆盖文件原来的内容
with open(filename, "a") as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n") 


filename = "python/guess.txt"
with open(filename, "w") as file_object:
    while True:
        name = input("Please input yur name: ")
        word = "Welcome your coming, " + name.title()
        print(word)
        file_object.write(word + "\n")

