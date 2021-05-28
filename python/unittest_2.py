# _*_coding:utf-8 _*_


# assertEqual(a, b) 核实a == b
# assertNotEqual(a, b) 核实a != b
# assertTrue(x) 核实x 为True
# assertFalse(x) 核实x 为False
# assertIn(item , list ) 核实 item 在 list 中
# assertNotIn(item , list ) 核实 item 不在 list 中


# 测试类
import unittest

class Employee():
    def __init__(self, name):
        self.name = name 
        self.salaries = []

    def show_name(self):
        print(name)

    def give_raise(self, new_salary):
        self.salaries.append(new_salary)

    def show_salary(self):
        print("Salary raise: ")
        for salary in self.salaries:
            print("- " + salary)

name = "Judy"
my_salary = Employee(name)
my_salary.show_name()
# while True:
#     new_salary = input("Salary: ")
#     if new_salary == "q":
#         break
#     my_salary.give_raise(new_salary)
my_salary.give_raise("1000")
my_salary.show_salary()




# class TestSalary(unittest.TestCase):
#     def test_salary(self):
#         name = "Judy"
#         my_salary = Employee(name)
#         my_salary.give_raise("5000")

#         self.assertIn("5000", my_salary.salaries)


#     def test_salaries(self):
#         name = "Jessica"
#         my_salary = Employee(name)
#         salaries = ["1000", "2000", "3000"]
#         for salary in salaries:
#             my_salary.give_raise(salary)

#         for salary in salaries:
#             self.assertIn(salary, my_salary.salaries)

# unittest.main()

class TestSalary(unittest.TestCase):
    def setUp(self):
        name = "Judy"
        self.my_salary = Employee(name)
        self.salaries = ["1000", "2000", "3000"]

    def test_salary(self):
        self.my_salary.give_raise(self.salaries[0])
        self.assertIn(self.salaries[0], self.my_salary.salaries)
        # print(self.my_salary.salaries)

    def test_salaries(self):
        for salary in self.salaries:
            self.my_salary.give_raise(salary)
        for salary in self.salaries:
            self.assertIn(salary, self.my_salary.salaries)
        # print(self.my_salary.salaries)

unittest.main()

