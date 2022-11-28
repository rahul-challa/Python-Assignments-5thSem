'''
Write a program that prints Armstrong numbers in the range 1 to 1000. An Armstrong number is a
number whose sum of the cubes of the cubes of the digits is equal to the number itself. For Example,
370 = 3^3 + 7^3 + 0^3
'''
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")