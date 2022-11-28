'''
Write an assignment statement using a single conditional expression for the following if-else code:
if marks >= 70:
remarks = 'good'
else:
remarks = 'average'
'''
marks = (int(input()))
print({True:"good",False:"average"}[marks>=70])