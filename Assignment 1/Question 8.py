'''
Construct logical expressions for representing the following conditions:
a. marks scored should be greater than 300 and less than 400.
b. Whether the value of grade is an uppercase letter.
c. The post is engineer and experience is more than four years.
'''
marks = int(input("Enter Marks: "))
if(marks>300 and marks<400):
    print("true")
grade = input("Enter the Grade: ")
if(grade.isupper):
    print("true")
post = input("Enter Post: ")
exp = int(input("Enter Experience year: "))
if(post=='engineer' and exp>4):
    print("true")