# 简单判断语句
>>> car=["audi", 'bmw', "subaru", "toyato"] 
>>> cars=["audi", 'bmw', "subaru", "toyato"] 
>>> for car in cars:
...     if car == "bmw":
...             print(car.upper())
...     else:
...             print(car.title())
... 
Audi
BMW
Subaru
Toyato

# 字符串判断
>>> car = "audi" 
>>> car == "Audi" 
False
>>> car == "audi" 
True
>>> car.upper() == "Audi" 
False
>>> car.title() == "Audi" 
True
>>> car.upper() != "Audi" 
True

# 数值判断
>>> age_0 = 22
>>> age_1 = 21 
>>> (age_0 >= 21) and (age_1 >= 21)
True
>>> (age_0 >= 21) and (age_1 >= 22) 
False
>>> (age_0 >= 21) or (age_1 >= 22)  
True

# 包含，不包含
>>> banned_users = ['andrew', 'carolina', 'david']
>>> "candy" in  banned_users
False
>>> "candy" not in  banned_users 
True

# 布尔表达式
>>> car = 'subaru'
>>> print("Is car == 'subaru'? I predict True.")
Is car == 'subaru'? I predict True.
>>> print(car == 'subaru')
True
>>> print("\nIs car == 'audi'? I predict False.")

Is car == 'audi'? I predict False.
>>> print(car == 'audi')
False

>>> age = 19
>>> if age >= 18:
...     print("you are an adult!")
... 
you are an adult!

>>> age = 12
>>> if age < 4:
...     print("you need pay $0")
... elif  4 <= age < 18:
...     print("you need pay $5")
... else:
...     print("you need pay $10")
... 
you need pay $5

>>> alien_color="green" 
>>> if alien_color == "green":
...     score=5
... elif alien_color == "yellow":
...     score=10
... elif alien_color == "red":
...     score=15
... 
>>> print("you can get " + str(score) + " coins!") 
you can get 5 coins!

>>> users=["admin", "cindy", "marry", "jessica", "vivian"] 
>>> if users:
...     for user in users:
...             if user == "admin":
...                     print("Hello " + user + ", would you like to see a status report?")
...             else:
...                     print("Hello " + user + ", thank you for logging again.")
... else:
...     print("We need to find some users!")
... 
Hello admin, would you like to see a status report?
Hello cindy, thank you for logging again.
Hello marry, thank you for logging again.
Hello jessica, thank you for logging again.
Hello vivian, thank you for logging again.

>>> current_users=["admin", "cindy", "marry", "jessica", "vivian"]  
>>> new_users=["may", "lily", "admin", "vivian", "judy"] 
>>> for new_user in new_users:
...     if new_user in current_users:
...             print("Please give a new name")
...     else:
...             print("This is a new name")
... 
This is a new name
This is a new name
Please give a new name
Please give a new name
This is a new name

>>> for num in range(1,10):
...     if num == 1:
...             print(str(num)+"st")
...     elif num == 2:
...             print(str(num)+"nd")
...     elif num == 3:
...             print(str(num)+"rd")
...     else:
...             print(str(num)+"th")
... 
1st
2nd
3rd
4th
5th
6th
7th
8th
9th

