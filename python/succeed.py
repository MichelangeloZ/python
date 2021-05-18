# _*_coding:utf-8 _*_

class Car(object):
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
        print(self.make + " has " + str(self.odometer_reading) + " miles on it.")

    def fill_gas_tank(self, gas_type):
        print(self.make + " need fill " + str(gas_type) + " oil.")

# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         # python2.7 中的继承，函数super() 需要两个实参：子类名和对象self
#         super(ElectricCar, self).__init__(make, model, year)

class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size == 85

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性""" 
        # python3中的继承
        super().__init__(make, model, year)
        # 初始化子类的特有属性
        # self.battery_size = 70
        # 将实例用作属性
        self.battery = Battery()

    # 子类特有的方法
    # def describle_battery(self):
    #     print(self.make + " has a " + str(self.battery_size) + "-kWh battery.")

    # 重写父类的方法，对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写
    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("Electric car doesn't need a gas tank!")

my_car = Car("audi", "A8", 2018)
my_car.read_odometer()
my_car.fill_gas_tank(92)

my_tesla = ElectricCar("tesla", "models s", 2016)
# 继承父类的方法
print(my_tesla.get_descriptive_name())

# 调用子类的方法
# my_tesla.describle_battery()

# 将实例用作属性
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# 重写父类方法
my_tesla.fill_gas_tank()



## 练习

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print("\nThis restaurant's name is " + self.restaurant_name)
        print("This restaurant's cuisine_type is " + self.cuisine_type)

    def open_restaurant(self):
        print("This restaurant is opening!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["straberry", "chocolate", "mongo", "grape"]

    def get_flavors(self):
        print("There are 4 kinds of flavors: ")
        print([flavor for flavor in self.flavors])

    def open_restaurant(self):
        print("This restaurant is not opening in winter!")

icecream = IceCreamStand("Summer", "cool")
icecream.describe_restaurant()
icecream.open_restaurant()
icecream.get_flavors()


class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("\nMy first_name is " + self.first_name.title() + ", my last_name is " + self.last_name.title())

class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Admin has these privileges: ")
        print([privilege for privilege in self.privileges])

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name, last_name)
        self.privilege = Privileges()

admin = Admin("jay", "chou")
admin.describe_user()
admin.privilege.show_privileges()

