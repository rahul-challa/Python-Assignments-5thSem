'''
Write a function to multiply two non-negative numbers by repeated addition, for example, 7*5 =
7+7+7+7+7.
'''
def multiply(m,n):
	if(n == 0):
		return 0
	return (m + multiply(m, n - 1))
m = int(input("Enter number m: "))
n = int(input("Enter number n: "))
print(multiply(m,n))