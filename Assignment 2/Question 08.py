'''
Write a function to print the table of entered number
'''
def table(number):
    for i in range(1,11):
        print(number,'x',i,'=',number*i)

if __name__=='__main__':
    table(int(input("Enter the number whose table you want: ")))