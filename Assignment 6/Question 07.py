'''
Examine the following string:
greeting = 'Good Morning. Have a Good Day!!'
What will be the output for the following function calls:
a. greeting.count('Good')
b. greeting.find('a')
c. greeting.rfind('a')
d. greeting.capitalize()
e. greeting.lower()
f. greeting.upper()
g. greeting.swapcase()
h. greeting.istitle()
i. greeting.replace('Good', 'Sweet')
j. greeting.strip()
k. greeting.split()
l. greeting.partition('.')
m. greeting.startswith('good')
n. greeting.endswith('!!')
'''
greeting = 'Good Morning. Have a Good Day!!'
print(greeting.count('Good'))
print(greeting.find('a'))
print(greeting.rfind('a'))
print(greeting.capitalize())
print(greeting.lower())
print(greeting.upper())
print(greeting.swapcase())
print(greeting.istitle())
print(greeting.replace('Good', 'Sweet'))
print(greeting.strip())
print(greeting.split())
print(greeting.partition('.'))
print(greeting.startswith('good'))
print(greeting.endswith('!!'))