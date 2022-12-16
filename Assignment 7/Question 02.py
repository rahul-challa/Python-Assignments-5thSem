'''
Write a function that takes a list of numbers as input from the user and produces the corresponding
cumulative list where each element in the list at index i is the sum of elements at index j <= i.
'''
def sum(list):
    result = []                                  # list to store result elements
    sum = 0
    for i in list:                               # for i
        sum += i                                 # add all elements =< i
        result.append(sum)                       # getting result list
    return result
def main():
    list =[]                                     # list for taking user input
    size = int(input("Input length of list :"))  # taking input size of list 
    for j in range (size):                        
        k = int(input("Enter the element :"))    
        list.append(k)                           
    print("Your list is :",list)                 # user input list
    print("The result list is :",sum(list))      # result list
if __name__=='__main__':
    main()