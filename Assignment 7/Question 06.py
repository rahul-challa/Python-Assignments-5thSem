'''
Write a function that takes n as an input and creates a list of n lists such that ith list contains first five multiples of i.
'''
n = int(input("Enter the value of n :"))

for i in range(1,n+1):
    list =[]
    print("for value of i = :",i)
    for j in range(1,6):
        k = i*j
        list.append(k)
    print(list)