'''
Write a python program to perform the following tasks:
1. Reverse a string
2. Reverse a string without reversing the words. Example:
    input data: 'welcome to iter'
    output: 'iter to welcome'
3. Check if a string is symmetric or asymmetric
4. Check if a string is palindrome.
5. Given a string s and index i, delete ith value from s
6. Count the number of vowels and consonants in a string.
7. Find length of a string without using inbuilt function.
8. Check if a string contains at least one digit and one alphabet.
9. Remove duplicates from a string.
10. Count frequency of characters in a string.
11. Find the character having maximum frequency in a string.
12. Check if a pair of strings are anagram to each other. Example: SILENT and LISTEN are ana-
grams.
'''
def a1(str):
    print(str[::-1])
def a2(str):
    list = str.split()
    print("".join(list[::-1]))
def a3(str):
    if str[:len(str)//2]==str[(len(str)//2):]:
        print("Symmetric")
    else:
        print("Asymmetric")
def a4(str):
    if str == str[::-1]:
        print("Paliondrome")
    else:
        print("Not a Palindrome")
def a5(str,i):
    print(str[:i]+str[i+1:])
def a6(str,vowel):
    str = str.lower()
    list = [each for each in str if each in vowel]
    print(len(list),"",len(str)-len(list))
def a7(str):
    c=0
    for i in str:
        c+=1
    print(c)
def a8(str):
    print(str.isalnum())
def a9(str):
    print("".join(set(str)))
def a10(str):
    temp = {}
    for i in temp:
        if i in temp:
            temp[i]+=1
        else:
            temp[i]=1
    return temp
def a11(str):
    dict = a10(str)
    max_free = max(dict,key=dict.get)
    print(max_free)
def a12(str,str1):
    print(sorted(str)==sorted(str1))
if __name__=='__main__':
    a1("welcome to iter")
    a2("welcome to iter")
    a3("KhoKho")
    a4("amaama")
    a5("hello",2)
    a6("amaama","aeiou")
    a7("welcome to iter")
    a8("hey123")
    a9("amaama")
    print(a10("amaama"))
    a11("amaama")
    a12("silent","listen")