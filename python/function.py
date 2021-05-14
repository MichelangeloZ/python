 #_*_coding:utf-8 _*_
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



