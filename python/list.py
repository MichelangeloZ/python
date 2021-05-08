
# 访问列表元素
>>> bicycles = ['trek', 'cannondale', 'redline', 'specialized']
>>> print(bicycles)
['trek', 'cannondale', 'redline', 'specialized']
>>> print(bicycles[2]) 
redline
>>> print(bicycles[2].title()) 
Redline

# 练习字符串
>>> name="Eric" 
>>> msg="Hello " + name + ", would you liketo learn some Python today?" 
>>> print(msg) 
Hello Eric, would you liketo learn some Python today?
>>> print(name.title()) 
Eric
>>> print(name.upper()) 
ERIC
>>> print(name.lower()) 
eric
>>> name="Albert Einstein" 
>>> word='“Apersonwho never madea mistake never tried anything new.”' 
>>> print(name + " once said," + word) 
Albert Einstein once said,“Apersonwho never madea mistake never tried anything new.”
>>> name="    Bob     " 
>>> print(name) 
    Bob     
>>> print(name.lstrip()) 
Bob     
>>> name                
'    Bob     '
>>> name.lstrip()
'Bob     '
>>> name.rstrip() 
'    Bob'
>>> name.strip()  
'Bob'

# 练习整数
>>> print(3+5) 
8
>>> print(10-2) 
8
>>> print(2*4)  
8
>>> print(16/2) 
8.0

# 练习列表
>>> names=['Alice', 'Bob', 'Cindy', 'David', 'Ellen'] 
>>> names[0] 
'Alice'
>>> names[2]   
'Cindy'
>>> names[-1] 
'Ellen'
>>> print(names[3] + ", Welcome to my house!") 
David, Welcome to my house!

>>> transportation=["bike", "car", "bus", "taxi", "subway"] 
>>> print("I would like to own a " + transportation[1]) 
I would like to own a car

# 修改增加删除列表元素
>>> names
['Alice', 'Bob', 'Cindy', 'David', 'Ellen']
>>> names[0]="Judy"
>>> names
['Judy', 'Bob', 'Cindy', 'David', 'Ellen']
>>> names.append("Jessica") 
>>> names
['Judy', 'Bob', 'Cindy', 'David', 'Ellen', 'Jessica']
>>> names.insert(2, "Wendy") 
>>> names
['Judy', 'Bob', 'Wendy', 'Cindy', 'David', 'Ellen', 'Jessica']
>>> del names[2] 
>>> names
['Judy', 'Bob', 'Cindy', 'David', 'Ellen', 'Jessica']
>>> names.pop()
'Jessica'
>>> names
['Judy', 'Bob', 'Cindy', 'David', 'Ellen']
>>> names.remove("Bob") 
>>> names
['Judy', 'Cindy', 'David', 'Ellen']

# sort永久排序
>>> transportation.sort()
>>> print(transportation)
['bike', 'bus', 'car', 'subway', 'taxi']
>>> transportation.sort(reverse=True) 
>>> print(transportation)
['taxi', 'subway', 'car', 'bus', 'bike']
# sorted临时排序
>>> print(sorted(names,reverse=True)) 
['Judy', 'Ellen', 'David', 'Cindy']
>>> names
['Cindy', 'David', 'Ellen', 'Judy']
# 倒着打印列表
>> names.reverse()
>>> print(names) 
['Judy', 'Ellen', 'David', 'Cindy']
#获取列表长度
>>> len(names) 
4

>>> fruits=["cherry", "lemon", "banana", "grape", "apple", "mongo"] 
>>> len(fruits) 
6
>>> print(fruits.sorted()) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'sorted'
>>> print(sorted(fruits))  
['apple', 'banana', 'cherry', 'grape', 'lemon', 'mongo']
>>> print(sorted(fruits,reverse=True)) 
['mongo', 'lemon', 'grape', 'cherry', 'banana', 'apple']
>>> fruits
['cherry', 'lemon', 'banana', 'grape', 'apple', 'mongo']
>>> print(fruits.sort()) 
None
>>> fruits.sort()       
>>> fruits
['apple', 'banana', 'cherry', 'grape', 'lemon', 'mongo']
>>> fruits.sort(reverse=True) 
>>> fruits
['mongo', 'lemon', 'grape', 'cherry', 'banana', 'apple']
>>> fruits.reverse()
>>> fruits
['apple', 'banana', 'cherry', 'grape', 'lemon', 'mongo']
>>> len(fruits)   
6
>>> motorcycles = []
>>> print(motorcycles[-1])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range

# 遍历列表
>>> fruits=["cherry", "lemon", "banana", "grape", "apple", "mongo"]                            
>>> for fruit in fruits:
...     print(fruit)
... 
cherry
lemon
banana
grape
apple
mongo
>>> for fruit in fruits: 
...     print("I love eating " + fruit))
... 
I love eating cherry
I love eating lemon
I love eating banana
I love eating grape
I love eating apple
I love eating mongo

for fruit in fruits:           
     print("I love eating " + fruit)
print("How about you?")  

>>> for value in range(1,5):
...     print(value)
... 
1
2
3
4
>>> numbers = list(range(1,6))
>>> print(numbers)
[1, 2, 3, 4, 5]
>>> even_numbers = list(range(2,11,2))
>>> print(even_numbers)
[2, 4, 6, 8, 10]

>>> for value in range(1,11):
...     square=value**2
...     squares.append(square)
>>> print(squares) 
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

>>> for value in range(1,11):
...     squares.append(value**2)
>>> print(squares) 
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

>>> squares
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> min(squares) 
1
>>> max(squares) 
100
>>> sum(squares) 
385

# 列表解析
>>> squares=[value**2 for value in range(1,11)]
>>> print(squares) 
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

>>> num=[value for value in range(1,1000001)] 
>>> print(min(num)) 
1
>>> print(max(num)) 
1000000
>>> print(sum(num)) 
500000500000

>>> num=[value for value in range(3,31,3)] 
>>> print(num) 
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

>>> num=[value**3 for value in range(1,11)]   
>>> print(num)
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]


# 列表--切片




