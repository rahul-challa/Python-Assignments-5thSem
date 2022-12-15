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
    l1 = list()
    l2 = list()
    for i in range(0,5):
        l1.append(i)
        l2.append(i+3)
    print(l1)
    print(l2)
def func2():
    l1 = list()
    l2 = list()
    for i in range(0,5):
        l1.append(i)
        l2.append(i+3)
    l1, l2 = l2, l1
    print(l1)
    print(l2)
def main():
    print(func1())
    print(func2())
if __name__=='__main__':
    main()