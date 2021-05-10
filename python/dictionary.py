
# 获取字典值
>>> alien_0 = {'color': 'green', 'points': 5}
>>> print(alien_0['color'])
green
>>> print(alien_0['points'])
5
>>> alien_0['x_position'] = 0
>>> alien_0['y_position'] = 25 
>>> print(alien_0)             
{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
>>> alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
>>> print("Original x-position: " + str(alien_0['x_position']))
Original x-position: 0
>>> 
>>> 
>>> favorite_languages = {
... 'jen': 'python', 
... 'sarah': 'c',    
... 'edward': 'ruby',
... 'phil': 'python',
... }
>>> 
>>> favorite_languages['sarah']
'c'

# 字典遍历
>>> user_0 = {
... 'username': 'efermi',
... 'first': 'enrico',
... 'last': 'fermi',
... }
>>>

# 遍历键值对
>>> for key, value in user_0.items():
...     print("\nKEY: " + key)        
...     print("VALUE: " + value)))
... 

KEY: username
VALUE: efermi

KEY: first
VALUE: enrico

KEY: last
VALUE: fermi

# 遍历键
>>> favorite_languages = {
... 'jen': 'python',
... 'sarah': 'c',
... 'edward': 'ruby',
... 'phil': 'python',
... }
>>> for name in favorite_languages.keys():
...     print(name.title())
... 
Jen
Sarah
Edward
Phil

# 遍历值
>>> for language in favorite_languages.values(): 
...     print(language)
... 
python
c
ruby
python

>>> for name in favorite_languages.keys():
...     print(favorite_languages[name])
... 
python
c
ruby
python

# 按顺序遍历字典中的所有键
>>> for name in sorted(favorite_languages.keys()):
...     print(name)
... 
edward
jen
phil
sarah

# 遍历值去重
>>> for language in set(favorite_languages.values()):
...     print(language)
... 
c
ruby
python

>>> for name in favorite_languages.keys():
...     print(name + " likes learning " + favorite_languages[name])
... 
jen likes learning python
sarah likes learning c
edward likes learning ruby
phil likes learning python

names=["jen", "phil"]
>>> for user in  favorite_languages.keys():
...     if user in names:
...             print(user + " thanks for your attention")
...     else:
...             print(user + " you are invited")
... 
jen thanks for your attention
sarah you are invited
edward you are invited
phil thanks for your attention

# 有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套 。
# 你可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典。
>>> alien_0 = {'color': 'green', 'points': 5}
>>> alien_1 = {'color': 'yellow', 'points': 10}
>>> alien_2 = {'color': 'red', 'points': 15}
>>> aliens = [alien_0, alien_1, alien_2]
>>> for alien in aliens:
...     print(alien)
... 
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}

# 在字典中存储列表
>>> favorite_languages = {
... 'jen': ['python', 'ruby'],
... 'sarah': ['c'],
... 'edward': ['ruby', 'go'],
... 'phil': ['python', 'haskell'],
... }
>>> for name, languages in favorite_languages.items():
...     print("\n" + name.title() + "'s favorite languages are:")
...     for language in languages:
...             print("\t" + language.title())
... 

Jen's favorite languages are:
        Python
        Ruby

Sarah's favorite languages are:
        C

Edward's favorite languages are:
        Ruby
        Go

Phil's favorite languages are:
        Python
        Haskell
>>>

#  在字典中存储字典
>>> users = {
... 'aeinstein': {
... 'first': 'albert',
... 'last': 'einstein',
... 'location': 'princeton',
... },
... 'mcurie': {
... 'first': 'marie',
... 'last': 'curie',
... 'location': 'paris',
... },
... }
>>> for username, user_info in users.items():
...     print("\nUsername: " + username)
...     full_name = user_info['first'] + " " + user_info['last']
...     location = user_info['location']
...     print("\tFull name: " + full_name.title())
...     print("\tLocation: " + location.title())
... 

Username: aeinstein
        Full name: Albert Einstein
        Location: Princeton

Username: mcurie
        Full name: Marie Curie
        Location: Paris

       
# 练习
people = [ {'color': 'green', 'points': 5}, {'color': 'yellow', 'points': 10}, {'color': 'red', 'points': 15}]
>>> for value in people:
...     print(value)
... 
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}

people = { "Amily": ["北京", "上海", "广州"], "Bay" : ["西安", "武汉", "成都"], "Cindy" : ["杭州", "南京", "重庆"] }
>>> for person, cities in people.items(): 
...     for city in cities:
...             print(person + " : " + city)
... 
Amily : 北京
Amily : 上海
Amily : 广州
Bay : 西安
Bay : 武汉
Bay : 成都
Cindy : 杭州
Cindy : 南京
Cindy : 重庆

 cities = { "beijing" : {"country": "China", "population": "16B", "fact": "Forbiden City"}, 
 "NewYork" : {"country": "America", "population": "5B", "fact": "Statue of liberty"}, 
 "Paris" : {"country": "France", "population": "1B", "fact": "Notre-Dame of Paris"} }
 >>> for city, info in cities.items():
...     print("\nCity: " + city)      
...     print("\tCountry: " + info["country"])
...     print("\tPopulation: " + info["population"])
...     print("\tFact: " + info["fact"])
... 

City: beijing
        Country: China
        Population: 16B
        Fact: Forbiden City

City: NewYork
        Country: America
        Population: 5B
        Fact: Statue of liberty

City: Paris
        Country: France
        Population: 1B
        Fact: Notre-Dame of Paris