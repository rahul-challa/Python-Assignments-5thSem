def gcd(a,b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)
a,b = map(int,input("Enter the two numbers: ").split())
print("The gcd is : ",gcd(a,b))