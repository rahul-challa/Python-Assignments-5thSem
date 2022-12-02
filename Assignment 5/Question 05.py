'''
Study the program segments given below. Give the output produced, if any.
a = 4
def f():
    a = 5
    def g():
        nonlocal a
        a = 10
        print('inside function g,', 'a = ', a)
        def h():
            nonlocal a
            a = 20
            print('inside function h,', 'a = ', a)
        h()
    g()
    print('inside function f,', 'a = ', a)
f()
'''
a = 4
def f():
    a = 5
    def g():
        nonlocal a
        a = 10
        print('inside function g,', 'a = ', a)
        def h():
            nonlocal a
            a = 20
            print('inside function h,', 'a = ', a)
        h()
    g()
    print('inside function f,', 'a = ', a)
f()