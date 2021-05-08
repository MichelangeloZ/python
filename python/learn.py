
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