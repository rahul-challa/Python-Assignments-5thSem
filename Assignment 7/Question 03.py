'''
Write a program that takes a sentence as input from the user and computes the frequency of each
letter. Use a variable of dictionary type to maintain the count.
'''
sentence = input("Enter your sentence :")               # taking a sentence as input
frequency = {}                                          # defining a dictionary to store frequency
for i in sentence:
    if i in frequency:
        frequency[i] += 1                               # if letter is present adding 1
    else:
        frequency[i] = 1                                # first time letter encountered ==> count = 1
print("Count of all characters :\n ",frequency)         # printing the dictionary 