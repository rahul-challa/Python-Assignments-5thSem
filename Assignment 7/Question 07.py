'''
Write a function that takes a number as an input parameter and returns the correspond text in words,
for example, on input 452, the function should return 'Four Five Two'. Use a dictionary for mapping
digits to their string representation.
'''
'''
def conversion(n):
    dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 0: "zero"}
    l = []
    digits =[]
    digits = map(str,input().split())
    for i in range(len(digits)):
        j = dict[i]
        l.append(j)
    print(l)
def main():
    n = input("Input your number :")
    conversion(n)
if __name__=='__main__':
    main()
'''
def number_to_words(number):
    dict={"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine","0":"zero"}
    result=""
    for i in str(number):
        result+=dict[i]+" "
    result=result[:-1]
    print(result)
def main():
    number = input("Input your number :")
    number_to_words(number)
if __name__=='__main__':
    main()