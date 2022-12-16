'''
Given the following inputs, indicate in each case (a) to (w), whether the statements will execute
successfully. If, so, give what will be the outcome of execution? Also give the output of print
statements (where applicable):
address = 'B-6, Lodhi road, Delhi'
list1 = [1, 2, 3]
list2 = ['a', 1, 'z', 26, 'd', 4]
tuple1 = ('a', 'e', 'i', 'o', 'u')
tuple2 = ([2,4,6,8], [3,6,9], [4,8], 5)
dict1 = {'apple': 'red', 'mango': 'yellow', 'orange': 'orange'}
dict2 = {'X': ['eng', 'hindi', 'maths','science'], 'XII': ['english', 'physics','chemistry', 'maths']}
a.
list1[3] = 4
b.
print(list1 * 2)
c.
print(min(list2))
d.
print(max(list1))
e.
print(list(address))
f.
list2.extend(['e', 5])
print(list2)
g.
list2.append(['e', 5])
print(list2)
h.
names = ['rohan', 'mohan', 'gita']
names.sort(key= len)
print(names)
i.
list3 = [(x * 2) for x in range(1, 11)]
print(list3)
j.
del list3[1:]
print(list3)
k.
list4 = [ x+y for x in range(1,5) for y in range(1,5)]
print(list4)
l.
tuple2[3] = 6
m.
tuple2.append(5)
n.
t1 = tuple2 +(5)
o.
','.join(tuple1)
p.
list(zip(['apple', 'orange'], ('red','orange')))
q.
dict2['XII']
r.
dict2['XII'].append('computer science'),dict2
s.
'red' in dict1
t.
list(dict1.items())
u.
list(dict2.keys())
v.
dict2.get('XI', 'None')
w.
dict1.update({'kiwi':'green'})
print(dict1)
'''
address = 'B-6, Lodhi road, Delhi'
list1 = [1, 2, 3]
list2 = ['a', 1, 'z', 26, 'd', 4]
tuple1 = ('a', 'e', 'i', 'o', 'u')
tuple2 = ([2,4,6,8], [3,6,9], [4,8], 5)
dict1 = {'apple': 'red', 'mango': 'yellow', 'orange': 'orange'}
dict2 = {'X': ['eng', 'hindi', 'maths','science'], 'XII': ['english', 'physics','chemistry', 'maths']}
#a.
list1[3] = 4
print(list1[3])
#b.
print(list1 * 2)
#c.
print(min(list2))
#d.
print(max(list1))
#e.
print(list(address))
#f.
list2.extend(['e', 5])
print(list2)
#g.
list2.append(['e', 5])
print(list2)
#h.
names = ['rohan', 'mohan', 'gita']
names.sort(key= len)
print(names)
#i.
list3 = [(x * 2) for x in range(1, 11)]
print(list3)
#j.
del list3[1:]
print(list3)
#k.
list4 = [ x+y for x in range(1,5) for y in range(1,5)]
print(list4)
#l.
tuple2[3] = 6
print(tuple2[3])
#m.
tuple2.append(5)
print(tuple2)
#n.
t1 = tuple2 +(5)
print(t1)
#o.
','.join(tuple1)
print(tuple1)
#p.
print(list(zip(['apple', 'orange'], ('red','orange')))) 
#q.
dict2['XII']
print[dict2]
#r.
dict2['XII'].append('computer science'),dict2
print[dict2]
#s.
print('red' in dict1)
#t.
print(list(dict1.items()))
#u.
print(list(dict2.keys()))
#v.
print(dict2.get('XI', 'None'))
#w.
dict1.update({'kiwi':'green'})
print(dict1)