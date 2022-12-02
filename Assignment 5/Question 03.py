'''
Study the program segments given below. Give the output produced, if any.
globalVar = 10
def test():
    global globalVar
    localVar = 20
    globalVar = 30
    print('Inside function test : globalVar =', globalVar)
    print('Inside function test : localVar =', localVar)
test()
print('Outside function test : globalVar =', globalVar)
'''
globalVar = 10
def test():
    global globalVar
    localVar = 20
    globalVar = 30
    print('Inside function test : globalVar =', globalVar)
    print('Inside function test : localVar =', localVar)
test()
print('Outside function test : globalVar =', globalVar)