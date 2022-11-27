'''
Write a function named as 'UpperCase' which converts the lower case alphabet to uppercase alphabet.
Also, assert that the entered alphabet by user is valid lowercase alphabet. Write a function main that
accepts inputs from the user interactively and converts the lowercase alphabet to uppercase using the
function 'UpperCase'.
'''
def upperCase(str):
    assert str.islower()
    print(str.upper())
if __name__=='__main__':
    upperCase(input("Enter Lowercase alphabet: "))