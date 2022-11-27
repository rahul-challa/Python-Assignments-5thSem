'''
Write a function which takes co-ordinates of three points as input and returns true if points are
collinear otherwise returns false
'''
def collinear(x1,y1,x2,y2,x3,y3):
    a = x1*(y2-y3)+x3*(y3-y1)+x3*(y1-y2)
    if(a == 0):
        return("true")
    else:
        return("false")
x1,y1,x2,y2,x3,y3 = map(int,input("Enter the coordinates of the three points: ").split())
print(collinear(x1,y1,x2,y2,x3,y3))