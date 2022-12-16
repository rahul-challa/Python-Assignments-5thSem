'''
Write a function that takes n as an input and creates a list of n lists such that ith list contains first five multiples of i.
'''
class dictionary(dict):
    def __init__(self):
        self = dict()
    def add(self, key, value):
        self[key] = value
dict_obj = dictionary()
def result(n):
    for i in range(1,n+1):
        list =[]
        for j in range(1,6):
            k = i*j
            list.append(k)
        dict_obj.add(i,list)
    print(dict_obj)
def main():
    n = int(input("Enter the value of n :"))
    print(result(n))
if __name__=='__main__':
    main()