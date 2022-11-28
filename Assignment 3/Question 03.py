'''
Write a function to determine whether a given natural number is a perfect number. A natural number
is said to be a perfect number if it is the sum of its divisors. For Example, 6 is a perfect number
because 6 = 1+2+3, but 15 is not a perfect number because 15 != 1+3+5.
'''
def isPerfectNumber(n):
    sum = 1
    i = 2
    while i*i<=n:
        if n%i==0:
            sum = sum +i + n/i
        i+=1
    if (sum==n and n<=1):
        print(n," is a Perfect Number")
    else: 
        print(n," is not a Perfect Number")    
n = int(input("Enter any number: "))
isPerfectNumber(n)