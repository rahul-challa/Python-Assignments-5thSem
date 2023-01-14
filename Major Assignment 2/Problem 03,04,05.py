# Problem 03,04,05
import sys
active = True # used for repeating try block until we exit program

# Problem 03
# Creating class Student
class Student:
    # Problem 04
    # making the methods __init__ , moderate_marks , average , get_grade
    # __init__ contains the data members as asked in question 03
    def __init__(self, name, roll, python_mark, TOC_mark, OS_mark):
        self.name = name
        self.roll = roll
        self.python_mark = python_mark
        self.TOC_mark = TOC_mark
        self.OS_mark = OS_mark
        average_marks = 0
        grade = ""
    
    # moderate_marks used for adding grace marks 
    # if marks<100
    #   marks += grace
    #   if marks > 100
    #       marks = 100 
    # for all the subjects ensuring the max mark after grace is still not exceeding 100
    def moderate_marks(self, grace_mark):
        if (self.python_mark<100):         
            self.python_mark += grace_mark
            if(self.python_mark>100):
                self.python_mark = 100
        if (self.TOC_mark<100):
            self.TOC_mark += grace_mark
            if(self.TOC_mark>100):
                self.TOC_mark = 100
        if (self.OS_mark<100):
            self.OS_mark += grace_mark
            if(self.OS_mark>100):
                self.OS_mark = 100
        return self.python_mark,self.TOC_mark,self.OS_mark # returning marks with grace (new marks will be used for average)
    
    # average marks to get average of all the subject to use for grade valuation (uses marks updated with grace)
    def average(self):
        self.average_marks = (self.python_mark+self.TOC_mark+self.OS_mark)/3
        return self.average_marks
    
    # get_grade to evaluate the grade of the student 
    def get_grade(self):
        mark_percentage = (self.python_mark+self.TOC_mark+self.OS_mark)/3
        if mark_percentage < 40:
            self.grade = "D (Fail)"
        elif mark_percentage < 60:
            self.grade = "C"
        elif mark_percentage < 80:
            self.grade = "B"
        else:
            self.grade = "A"
        return self.grade

# input function to take valid input from 
def takeInput():
    try:
        studentDetails = {} # Student Details Dictionary
        studentDetails["name"] = userInput("\nEnter student name : ")
        studentDetails["roll"] = int(userInput("Enter roll number : "))
        marks = {} # Marks Dictionary
        marks["python_mark"] = int(userInput("Enter marks obtained in Python : "))
        marks["TOC_mark"]    = int(userInput("Enter marks obtained in TOC : "))
        marks["OS_mark"]     = int(userInput("Enter marks obtained in OS : "))
        studentDetails["marks"] = marks # Making the Nested Dictionary studentDetails = {"name":"","roll number":"","marks":{"python_name":"","TOC_mark":"","OS_mark":""}}
        assert len(studentDetails["name"]) > 0, "Name can't be empty" # checking the type of data entered 
        assert studentDetails["name"].isalpha, "Name can only contain alphabets"
        printStudentGrade(studentDetails) # printing the details 
    except:
        if active : # active used to check if the program is user terminated (this acts as a while true loop to take as many inputs as needed) 
            print(sys.exc_info()) # if(exception occurs and program is not terminated by user): print sys info and call input function again
            takeInput()

# function create object and display output
def printStudentGrade(studentDetails):
    # creating object from the user input
    stud = Student(studentDetails.get("name"),studentDetails.get("roll"),studentDetails.get("marks").get("python_mark"),studentDetails.get("marks").get("TOC_mark"),studentDetails.get("marks").get("OS_mark"))
    grace_mark = int(input("Enter the grace mark: ")) # taking input of grace mark from user
    # calling class methods
    print("Modetrate marks : ", stud.moderate_marks(grace_mark)) 
    print("average : ", stud.average())
    print("Grade : ", stud.get_grade())
    takeInput() # calling input function for next input

def userInput(message): # function to terminate program based on user input
    userInput = input(message)
    if str(userInput).lower() == "quit": # if user enters quit we exit the program
        global active
        active = False # making active = false so loop of input function is terminated
        print("------------------END OF PROGRAM------------------")
        quit()
    return userInput

def main():
    print("Enter \"Quit\" to quit this program") # giving user keyword to terminate program
    takeInput() # calling input function (runs in a loop until user enters "quit")

if __name__ == "__main__":
    main() # calling main function to start program execution