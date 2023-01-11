'''
PROGRAMMING IN PYTHON (CSE 3142)
MAJOR ASSIGNMENT - II
1   Objective
    The objective of the assignment is to provide programming practice regarding usage of python data structure
    and classes.
2   Problem Statement
    • Problem 1: Write python program to store student information using a nested dictionary “student”
    with key as follow:
    - name # String
    - roll # Integer
    - marks # Dictionary
    Further, the marks key should contains the marks for three different subjects. For example: student = {name : ”ABC”, roll : 1001, marks : {python mark: 99, TOC mark: 89, OS mark: 78}}
    Store the following database:
                    name roll pythonmark TOC mark OS mark
                    ABC  1001     99        89      78
                    EFG  1002     69        59      48
                    HIJ  1003     91        69      71
                    LMN  1004     89        78      67
    • Problem 2: Write a python code to store the dictionary to a pickle file “studentData”.
    • Problem 3: Write a python program to define a class “Student” that should contain the following
    data members:
    - name # String
    - roll # Integer
    - python mark # Integer
    - TOC mark # Integer
    - OS mark # Integer
    - average marks = 0 # This should be initialized to 0.
    - grade = “ ” # This should be initialized to empty string.
    • Problem 4: The class should support following methods:
    - init (): This is for initializing the data members.
    (Note: Only the first five data members should be passed by a user. for example:
        s1 = student(Name, Roll Number, Python, TOC, OS)
    The remaining two data members should be initialized in the init () itself.
    - moderate marks(grace mark): This should find the moderated marks for each subject using the
    formula:
        mark = mark + grace mark (1)
    Note: to avoid the situation where the moderated marks exceeds 100, reduce the moderated mark to 100 using the if-else statements.
    - average(): This should compute average marks obtained in the three subjects using the moderated marks. The update must be reflected in the data member “average marks”.
    - get grade(): This should update the data member “grade” using the grading matrix as follows:
    Mark percentage matrix Grade
    mark percentage < 40 D (Fail)
    40 <= mark percentage < 60 C
    60 <= mark percentage < 80 B
    80 <= mark percentage A
    • Problem 5: Read the data from dictionary student and store as object of the class Student. Print the
    grade for each student.
3   Mark Distribution
    • Problem 1 - [2 marks]
    • Problem 2 - [1 marks]
    • Problem 3 - [3 marks]
    • Problem 4 - [4 marks]
    • Problem 5 - [3 marks]
'''
import pickle

# Problem 1:

student = {
    "s1" : {
        "name" :"ABC", 
        "roll" : 1001, 
        "marks" : {"pythonmark": 99, "TOCmark": 89, "OSmark": 78}
        },
    "s2" : {
        "name" :"EFG", 
        "roll" : 1002, 
        "marks" : {"pythonmark": 69, "TOCmark": 59, "OSmark": 48}
        },
    "s3" : {
        "name" :"HIJ", 
        "roll" : 1003, 
        "marks" : {"pythonmark": 91, "TOCmark": 69, "OSmark": 71}
        },
    "s4" : {
        "name" :"LMN", 
        "roll" : 1004, 
        "marks" : {"pythonmark": 89, "TOCmark": 78, "OSmark": 67}
        }
}

# Problem 2:

with open('file.pickle', 'wb') as file:
    pickle.dump(student,file)
with open('file.pickle', 'rb') as file:
    unpickled = pickle.load(file)
    print(unpickled)

# Problem 3:

class Student:

# Problem 4:

    def __init__(self,name,rollNumber,python_mark,TOC_mark,OS_mark):
        self.name = name
        self.rollNumber = rollNumber
        self.python_mark = python_mark
        self.TOC_mark = TOC_mark
        self.OS_mark = OS_mark
    
    def moderate_marks(grace_mark,python_mark,TOC_mark,OS_mark):
        python_mark = python_mark + grace_mark
        TOC_mark = TOC_mark + grace_mark
        OS_mark = OS_mark + grace_mark
        if(python_mark>100):
            python_mark = 100
        if(TOC_mark>100):
            TOC_mark = 100
        if(OS_mark>100):
            OS_mark = 100
        return python_mark,TOC_mark,OS_mark
    
    def average(python_mark,TOC_mark,OS_mark):
        average_marks = (python_mark+TOC_mark+OS_mark)/3
        return average_marks

    def get_grade(python_mark,TOC_mark,OS_mark):
        grade = ""
        percentage = ((python_mark+TOC_mark+OS_mark)/300)*100
        if(percentage<40):
            grade = "D"
        elif(39<percentage<60):
            grade = "C"
        elif(59<percentage<80):
            grade = "B"
        elif(79<percentage):
            grade = "A"
        else:
            print("Invalid Grade")
        return grade