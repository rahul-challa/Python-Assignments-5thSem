'''
Write a function that takes a sentence as an input parameter and displays the number of words in the
sentence.
'''
def countWord(str):
    return str.count(" ")+1
print(countWord("Hello World, this is a example sentence"))