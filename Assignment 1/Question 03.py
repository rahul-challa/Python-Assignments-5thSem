'''
Evaluate the following expressions involving relational and logical operators:
a. 'hi' > 'hello' and 'bye' < 'Bye'
b. 'hi' > 'hello' or 'bye' < 'Bye'
c. 7 > 8 or 5 < 6 and 'I am fine' > 'I am not fine'
d. 10 !=9 and 29 >= 29
e. 10 !=9 and 29 >= 29 and 'hi' > 'hello' or 'bye' < 'Bye' and 7 <= 2.5
'''
print('hi' > 'hello' and 'bye' < 'Bye')                                      # (False and True) ==> False
print('hi' > 'hello' or 'bye' < 'Bye')                                       # (False and True) ==> True
print(7 > 8 or 5 < 6 and 'I am fine' > 'I am not fine')                      # (False or True) and (False) ==> False
print(10 !=9 and 29 >= 29)                                                   # (True and True) ==> True
print(10 !=9 and 29 >= 29 and 'hi' > 'hello' or 'bye' < 'Bye' and 7 <= 2.5)  # (True and True and False or False and False) ==> True