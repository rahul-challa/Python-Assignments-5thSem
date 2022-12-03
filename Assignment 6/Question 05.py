'''
Write a function that takes a string as an input and determines the count of the number of words
without using regular expression.
'''
def countWords(s):
    count = 1
    for i in s:
        if i==" ":
            count += 1
    return count
print(countWords("This is a Example Sentence"))