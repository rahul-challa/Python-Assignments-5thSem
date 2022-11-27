'''
Write a function areaTriangle that takes the lengths of three sides: side1, side2, and side3 of the
triangle as the input parameters and returns the area of the triangle as the output. Also, assert that sum
of the length of any two sides is greater than the third side. Write a function main that accepts inputs
from the user interactively and computes the area of the triangle using the function areaTriangle.
'''
def areaTriangle(side1,side2,side3):
    assert((side1 + side2 <=side3 ) or (side1 + side3 <= side2) or (side2 + side3 <= side1))
    s = (side1 + side2 + side3)/2
    print(s*(s-side1)*(s-side2)*(s-side3))**0.5

if __name__=='__main__':
    side1,side2,side3=map(float,input("enter the values of sides 1,2,3: ").split())
    areaTriangle(side1,side2,side3)