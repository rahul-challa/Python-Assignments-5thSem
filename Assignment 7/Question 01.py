'''
Write a function that takes a list of values as input parameter and returns another list without any
duplicates.
'''
list = []                                                            # list to store user input
length = int(input("Enter the length of your list :"))               # taking length of input list
for i in range(length):                                              
    print("Enter your number :")                                     # taking user input and storing in list
    j = input()
    list.append(j)
print ("Your list is : " + str(list))                                # printing the input list of user
resultList = []                                                      # result list for storing unique values
for i in list: 
    if i not in resultList: 
        resultList.append(i)                                         # adding elements that are unique 
print ("Your list after removing duplicates : " + str(resultList))   # printing the list