# _*_coding:utf-8 _*_
def greet(name):
    print("Hello! " + name)
greet("Jessica")

def display_message():
    print("I have learnt function")
display_message()
  
def favorite_book(title):
    print("One of my favorite books is " + title)
favorite_book("Alice in Wonderland")

def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(animal_type='cat', pet_name='Ketty')


# 形参指定默认值
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')
describe_pet('willie')

def make_shirt(size, word):
    print("\nT-shirt's size is " + size)
    print("there is " + word + " on the T-shirt.")
make_shirt(size="S", word="LINING" )

def make_shirt(size="L", word="I love Python"):
    print("\nT-shirt's size is " + size)
    print("there is " + word + " on the T-shirt.")
make_shirt()
make_shirt("M")
make_shirt(word="Good Morning")

def describle_city(city_name, country_name="China"):
    print(city_name + " is in " + country_name)
describle_city("shanghai")
describle_city(city_name="wuhan")
describle_city("Reykjavik", "Iceland")


# 函数返回值
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名""" 
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name 
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

返回字典
def make_album(singer, album, songs):
        if songs:
            return {"Singer": singer, "Album":"album", "Songs": "songs"}
        else:
            return {"Singer": singer, "Album":"album"}

while True:
    print("\nPlease tell some info about this album: ")
    print("(enter 'q' at any time to quit)")

    singer = input("Singer: ")
    if singer == "q":
        break
    album = input("Album: ")
    if album == "q":
        break
    songs = input("Songs: ")
    if songs == "q":
        break

    albums = make_album(singer, album, songs)


def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")


# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    #模拟根据设计制作3D打印模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)
# 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


def show_magicians(magicians):
    for magician in magicians:
        print(magician)

magicians = ["Abby", "Ben", "Cathay", "David"]
show_magicians(magicians)


传递列表练习
def make_great(magicians, great_magicians):
    while magicians:
        current = magicians.pop()
        print(current + " is the Great!")
        great_magicians.append(current)
    

def show_magicians(great_magicians):
    print("\nthese magicians are Great: ")
    for great in great_magicians:
        print(great)

magicians = ["Abby", "Ben", "Cathay", "David"]
great_magicians = []

make_great(magicians[:], great_magicians)
show_magicians(great_magicians)
print(magicians)


# 传递任意数量实参
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
    "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last 
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)


def car_info(brand, type, **message):
    info = {}
    info["brand"] = brand
    info["type"] = type
    for key, value in message.items():
        info[key] = value
    return info

info = car_info("BMW", "SUV", color="blank", location="China")
print(info)

# 函数导入方式
# 导入整个模块
import module_name
# 导入特定的函数
import module_name.function_name()
from module_name import function_name
# 从模块中导入任意数量的函数
from module_name import function_0, function_1, function_2
# 使用as 给函数指定别名
from module_name import function_name as fn
# 给模块指定别名
import module_name as mn
# 导入模块中的所有函数
from module_name import *
