'''
Write a function that returns True or False depending on whether the given number is a palindrome
'''
def isPalindrome(word):
    return word == word[::-1]
n = input("Enter Input: ")
print(isPalindrome(n))