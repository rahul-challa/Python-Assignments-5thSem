'''
Write a program that takes a sentence as input from the user and computes the frequency of each
letter. Use a variable of dictionary type to maintain the count.
'''
sentence = input("Enter your sentence :")
frequency = {}
for i in sentence:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1 
print("Count of all characters :\n " + str(frequency))