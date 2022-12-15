'''
Write a function that takes a list of values as input parameter and returns another list without any
duplicates.
'''
list = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9] 
print ("The list is: " + str(list)) 

resultList = [] 
for i in list: 
    if i not in resultList: 
        resultList.append(i) 

print ("The list after removing duplicates : " + str(resultList)) 