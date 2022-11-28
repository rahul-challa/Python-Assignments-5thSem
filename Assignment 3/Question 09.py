'''
Write a function that returns the sum of digits of a number, passed to it as an argument.
'''
def printSum(n):
    s=0
    for i in n:
        s=s+int(i)
    print (s)
n=input("Enter the number")
printSum(n)