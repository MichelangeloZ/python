# _*_coding:utf-8 _*_

class Car():

    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        # 给属性指定默认值
        self.odometer_reading = 5

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# 修改属性的值
# 1. 直接修改属性的值
my_new_car.odometer_reading = 23

# 2. 通过方法修改属性的值
my_new_car.update_odometer(35)

# 通过方法对属性的值进行递增'
my_new_car.increment_odometer(100)

my_new_car.read_odometer()



class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("\nThis restaurant's name is " + self.restaurant_name)
        print("This restaurant's cuisine_type is " + self.cuisine_type)

    def open_restaurant(self):
        print("This restaurant is opening!")

    def people_served(self):
        print("This restaurant has served " + str(self.number_served) + " people.")

    def set_number_served(self, person):
        self.number_served = person

    def increment_number_served(self, people):
        self.number_served += people


reataurant = Restaurant("Enjoy Life", "freestyle")
reataurant.describe_restaurant()
reataurant.open_restaurant()

reataurant.set_number_served(5)
reataurant.increment_number_served(25)
reataurant.people_served()


class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("\nMy first_name is " + self.first_name.title() + ", my last_name is " + self.last_name.title())

    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " +  self.last_name.title())

    def get_users(self):
        print("\nUser has attempted login " + str(self.login_attempts) + " times")

    def increment_login_attempts(self, count):
        self.login_attempts += count

    def reset_login_attempts(self, num):
        self.login_attempts = num

user = User("jay", "chou")
user.describe_user()
user.greet_user()

user.increment_login_attempts(1)
user.reset_login_attempts(0)
user.get_users()

