'''
What will be the output on executing each of the statements, following the assignment statement:
address = 'B-6, Lodhi road, Delhi'
a. len(address)
b. address[17:-1]
c. address[-len(address): len(address)]
d. address[:-12] + address[-12:]
e. address.find('delhi')
f. address.swapcase()
g. address.split(',')
h. address.isalpha()
'''
address = 'B-6, Lodhi road, Delhi'
print(len(address))
print(address[17:-1])
print(address[-len(address): len(address)])
print(address[:-12] + address[-12:])
print(address.find('delhi'))
print(address.swapcase())
print(address.split(','))
print(address.isalpha())