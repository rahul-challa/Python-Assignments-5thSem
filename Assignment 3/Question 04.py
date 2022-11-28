def LCM(x,y):
    if x>y:
        a = x
    else:
        a = y
    while(True):
        if((a%x==0)and(a%y==0)):
            LCM = a
            break
        a =+ 1
    return LCM
x,y=map(int,input("Enter the values of m and n: ").split())
print("The LCM is ",LCM(x,y))