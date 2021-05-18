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

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性""" 
        # python3中的继承
        super().__init__(make, model, year)
        # 初始化子类的特有属性
        self.battery_size = 70

    # 子类特有的方法
    def describle_battery(self):
        print(self.make + " has a " + str(self.battery_size) + "-kWh battery.")

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
my_tesla.describle_battery()

# 重写父类方法
my_tesla.fill_gas_tank()

