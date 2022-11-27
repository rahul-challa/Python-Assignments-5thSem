'''
How does the effect of the following two statements differ?
a. x += x + 10
b. x = x+ 10
'''
x = int(input("Enter x: "))
a = x
x += x+10
print(x)
x = a
x = x+10
print(x)