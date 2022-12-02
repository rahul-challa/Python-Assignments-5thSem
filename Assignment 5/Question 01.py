'''
Study the program segments given below. Give the output produced, if any.
globalVar = 10
def test():
    localVar = 20
    print('Inside function test : globalVar=', globalVar)
    print('Inside function test : localVar =', localVar)
test()
print('Outside function test : globalVar =', globalVar)
print('Outside function test : localVar =', localVar)
'''
globalVar = 10
def test():
    localVar = 20
    print('Inside function test : globalVar=', globalVar)
    print('Inside function test : localVar =', localVar)
test()
print('Outside function test : globalVar =', globalVar)
print('Outside function test : localVar =', localVar)