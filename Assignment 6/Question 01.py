'''
Write a function that takes a string as a parameter and returns a string with every successive repetitive
character replaced with a star(*). For example, 'balloon' is returned as 'bal*o*n'.
'''
def replaceWithStar(str):
    strres = ''
    for i in range(0,len(str)):
        if str[i]==str[i-1]:
            strres = strres[:i+1]+'*'
        else:
            strres += str[i]
    return strres
print(replaceWithStar('balloon'))