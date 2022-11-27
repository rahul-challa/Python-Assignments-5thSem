'''
Find the sum of even digits of a four-digit number using function.
Warning: Don't use control structures.
'''
number = int(input("Enter your 4 digit number: "))
x = 0
digit = number//1000
x += (1-digit%2) + digit
digit1 = (number-digit*1000)//100
x += (1-digit1%2) + digit1
digit2 = (number-digit*1000-digit1*100)//10
x += (1-digit1%2) + digit2
digit3 = (number-digit*1000-digit1*100-digit2*10)
x += (1-digit%3)*digit3
print(x)