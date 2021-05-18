# _*_coding:utf-8 _*_

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " is now sitting!")
    def rool_over(self):
        print(self.name.title() + " rolled over" )

# 根据类创建实例
my_dog = Dog("jerry", 5)

# 访问实例属性
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# 调用方法
my_dog.sit()
my_dog.rool_over()


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\nThis restaurant's name is " + self.restaurant_name)
        print("This restaurant's cuisine_type is " + self.cuisine_type)

    def open_restaurant(self):
        print("This restaurant is opening!")

my_reataurant = Restaurant("Enjoy Life", "freestyle")
my_reataurant.describe_restaurant()
my_reataurant.open_restaurant()

your_restaurant = Restaurant("Oceanline", "sweet")
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()

class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print("\nMy first_name is " + self.first_name.title() + ", my last_name is " + self.last_name.title())
    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " +  self.last_name.title())

user = User("jay", "chou")
user.describe_user()
user.greet_user()

    
# 运行结果
My dog's name is Jerry.
My dog is 5 years old.
Jerry is now sitting!
Jerry rolled over

This restaurant's name is Enjoy Life
This restaurant's cuisine_type is freestyle
This restaurant is opening!

This restaurant's name is Oceanline
This restaurant's cuisine_type is sweet
This restaurant is opening!

My first_name is Jay, my last_name is Chou
Hello, Jay Chou
