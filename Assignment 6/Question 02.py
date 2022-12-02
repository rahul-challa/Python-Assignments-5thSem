'''
Write a function that takes two strings and returns True if they are anagrams and False otherwise. A
pair of strings is anagrams if the letters in one word can be arranged to form the second one.
'''
def anagram(str,str1):
    resstr = ''.join(sorted(str))
    resstr1 = ''.join(sorted(str1))
    if(resstr == resstr1):
        return True
    else:
        return False
print(anagram("kutta","tutka"))