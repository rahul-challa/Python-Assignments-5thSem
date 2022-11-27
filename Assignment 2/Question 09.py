'''
Study the program segments given below. Give the output produced, if any.
a.  def say (message, times=2):
        print(message*times)
        say ('Hello')
        say('World',5)
b.  def fun(a=2,b=3,c=7):
        d= a+b+c
        print(d)
        print(fun (2))
'''
def say (message, times=2):
        print(message*times)
        say ('Hello')
        say('World',5)
def fun(a=2,b=3,c=7):
        d= a+b+c
        print(d)
        print(fun (2))