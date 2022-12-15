'''
Determine the output of the following code snippets:
1.
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = 0
for i in range(0, 10):
    if (c[i]%2 == 0):
        result += c[i]
print(result)
2.
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = 0
for i in range(0, 10):
    if (c[i]%2 != 0):
        result += c[i]
print(result)
3.
subject = 'computer'
subject = list(subject)
ch = subject[0]
for i in range(0, len(subject)-1):
    subject[i] = subject[i+1]
    subject[len(subject)-1]=ch
print(''.join(subject))
4.
quantity = [15, 30, 12, 34, 56, 99]
total = 0
for i in range(0, len(quantity)):
    if (quantity[i] > 15):
        total += quantity[i]
print(total)
5.
x = [1, 2, 4, 6, 9, 10, 14, 15, 17]
for i in range(0, len(x)):
    if (x[i]%2 == 0):
        x[i] = 4*i
    elif (x[i]%3 == 0):
        x[i] = 9*i
    else:
        x[i] *= 2
print(x)
'''
def function1():
    c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = 0
    for i in range(0, 10):
        if (c[i]%2 == 0):
            result += c[i]
    print(result)

def function2():
    c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = 0
    for i in range(0, 10):
        if (c[i]%2 != 0):
            result += c[i]
    print(result)

def function3():
    subject = 'computer'
    subject = list(subject)
    ch = subject[0]
    for i in range(0, len(subject)-1):
        subject[i] = subject[i+1]
        subject[len(subject)-1]=ch
    print(''.join(subject))

def function4():
    quantity = [15, 30, 12, 34, 56, 99]
    total = 0
    for i in range(0, len(quantity)):
        if (quantity[i] > 15):
            total += quantity[i]
    print(total)

def function5():
    x = [1, 2, 4, 6, 9, 10, 14, 15, 17]
    for i in range(0, len(x)):
        if (x[i]%2 == 0):
            x[i] = 4*i
        elif (x[i]%3 == 0):
            x[i] = 9*i
        else:
            x[i] *= 2
    print(x)

def main():
    function1()
    print("---------------------------------------")
    function2()
    print("---------------------------------------")
    function3()
    print("---------------------------------------")
    function4()
    print("---------------------------------------")
    function5()

if __name__=='__main__':
    main()