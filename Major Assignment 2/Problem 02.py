# Problem 02
# output file not included in ZIP file and will be created during execution
import sys
import pickle

active = True # used for repeating try block until we exit program
file = open("file2.txt", "wb") # opening file in write mode

def takeInput(): # function to take valid inputs
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
        write(studentDetails) #calling the Write Function
    except:
        if active : # active used to check if the program is user terminated (this acts as a while true loop to take as many inputs as needed) 
            print(sys.exc_info()) # if(exception occurs and program is not terminated by user): print sys info and call input function again
            takeInput() 

def write(studentDetails): # function to take input and write it in file
    pickle.dump(studentDetails, file) # dumping data into file
    file.flush() # clearing buffer for next input
    takeInput() # call input to take next input

def userInput(message): # function to terminate program based on user input
    userInput = input(message)
    if str(userInput).lower() == "quit": # if user enters quit we exit the program
        global active
        active = False # making active = false so loop of input function is terminated
        print("The binary dumps are stored in \"file2.txt\"")
        print("------------------END OF PROGRAM------------------")
        quit()
    return userInput

def main():
    print("Enter \"Quit\" to quit this program") # giving user keyword to terminate program
    takeInput() # calling input function (runs in a loop until user enters "quit")

if __name__ == "__main__":
    main() # calling main function to start program execution