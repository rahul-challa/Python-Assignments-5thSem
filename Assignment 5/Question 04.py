'''
Study the program segments given below. Give the output produced, if any.
def test1():
    test1.a = 10
    def test2():
        test1.a = 8
        print('Inside function test2: ', test1.a)
    test2()
    print('Outside function test2 ', test1.a)
test1()
'''
def test1():
    test1.a = 10
    def test2():
        test1.a = 8
        print('Inside function test2: ', test1.a)
    test2()
    print('Outside function test2 ', test1.a)
test1()