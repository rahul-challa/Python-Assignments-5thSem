'''
Write a function that takes a list of numbers as input from the user and produces the corresponding
cumulative list where each element in the list at index i is the sum of elements at index j <= i.
'''
def rock(list):
    result = []
    sum = 0
    for i in list:
        sum += i
        result.append(sum)
    return result
def main():
    list =[]
    size = int(input("Input length of list :"))
    for j in range (size):
        k = int(input("Enter the element :"))
        list.append(k)
    print(rock(list))
if __name__=='__main__':
    main()