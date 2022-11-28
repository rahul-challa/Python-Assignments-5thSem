'''
Write a function that takes two numbers as input parameters and returns True or False depending on
whether they are co-primes. Two numbers are said to be co-prime if they do not have any common
divisor other than one.
'''
def coprime(m,n):
    gcd = 1
    for i in range(1, m+1):
        if m%i==0 and n%i==0:
            gcd = i
    return (True if gcd == 1 else False)
m = int(input("Enter number m: "))
n = int(input("Enter number n: "))
print(coprime(m,n))