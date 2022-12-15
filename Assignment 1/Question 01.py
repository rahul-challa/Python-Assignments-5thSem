'''
Evaluate the following expressions:
(x<y) or (not(z==y) and (z<x))
a. x =0, y=6, z=10
b. x=1, y=1, z=1
'''
x,y,z = 0,6,10
print(x<y)                  # x<y => 0<6 => True
print(not(z==y) and (z<x))  # ((not(z==y) => not(10==6) => not(False) => True) and (z<x) => (10<0) => False)) => True and False => False

x,y,z = 1,1,1
print(x<y)                  # x<y => 1<1 => False
print(not(z==y) and (z<x))  # (not(z==y) => not(1==1) => not(True) => False) and (z<x) => (1<1) => False)) => False and False => False 