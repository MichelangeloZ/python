
>>> current_number = 1         
>>> while current_number <= 5:
...     print(current_number)
...     current_number += 1
... 
1
2
3
4
5


>>> current_number = 0
>>> while current_number < 10:
...     current_number += 1
...     if current_number % 2 == 0:
...             continue
...     print(current_number)
... 
1
3
5
7
9

# 练习
>>> prompt="\nwhat kind of fruits do you like?" 
>>> prompt+="\nEnter 'quit' to end the program." 
>>> active = True 
>>> while active:
...     message=input(prompt)
...     if message == "quit":
...             active = False
...     else:
...             print(message)
... 

what kind of fruits do you like?
Enter 'quit' to end the program.banana
banana

what kind of fruits do you like?
Enter 'quit' to end the program.apple
apple

what kind of fruits do you like?
Enter 'quit' to end the program.quit
>>>

>>> while True:
...     message=input(prompt)
...     if message == "quit":
...             break
...     else:
...              print(message)
... 

what kind of fruits do you like?
Enter 'quit' to end the program.cherry
cherry

what kind of fruits do you like?
Enter 'quit' to end the program.quit


>>> prompt="\nHow old are you:"          
>>> while True:
...     message = input(prompt)
...     if int(message) < 3:
...             print("you need pay 0$")
...     elif 3 <= int(message) < 12:
...             print("you need pay 10$")
...     else:
...             print("you need pay 15$")
... 

How old are you:1
you need pay 0$

How old are you:5
you need pay 10$

How old are you:18
you need pay 15$

How old are you:Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt


# 删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
  pets.remove('cat')
print(pets)

['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
['dog', 'dog', 'goldfish', 'rabbit']


# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
  current_user = unconfirmed_users.pop()
  print("Verifying user: " + current_user.title()) 
  confirmed_users.append(current_user)
# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
  print(confirmed_user.title())

Verifying user: Candace
Verifying user: Brian
Verifying user: Alice
The following users have been confirmed:
Candace
Brian
Alice
