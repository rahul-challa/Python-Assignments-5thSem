'''
Identify the output produced when the following functions are invoked.
1.
def func():
    l1 = list()
    l2 = list()
    for i in range(0,5):
        l1.append(i)
        l2.append(i+3)
    print(l1)
    print(l2)
2.
def func():
    l1 = list()
    l2 = list()
    for i in range(0,5):
        l1.append(i)
        l2.append(i+3)
    l1, l2 = l2, l1
    print(l1)
    print(l2)
'''
def func1():
    l1 = list()           # defining lists
    l2 = list()           
    for i in range(0,5):
        l1.append(i)      # adds the elements [0,1,2,3,4]
        l2.append(i+3)    # adds the elements [0+3,1+3,2+3,3+3,4+3]
    print(l1)             # printing lists
    print(l2)
def func2():
    l1 = list()           # definign lists
    l2 = list()
    for i in range(0,5):   
        l1.append(i)      # adds the elements [0,1,2,3,4]
        l2.append(i+3)    # adds the elements [0+3,1+3,2+3,3+3,4+3]
    l1, l2 = l2, l1       # swapping the values of the lists
    print(l1)
    print(l2)
def main():
    print(func1())        # calling functions
    print(func2())
if __name__=='__main__':
    main()