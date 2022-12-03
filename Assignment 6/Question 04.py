'''
Write a function that takes a sentence as an input parameter and replaces the first letter of every word
with the corresponding uppercase letter and rest of the letters in the word by corresponding letters in
lowercase without using builtin function.
'''
def convert(str):
    ch = list(str)
    for i in range(len(str)):
        if(i==0 and ch[i]!='' or ch[i]<='z'):
            ch[i]=chr(ord(ch[i]-ord('a')+ord('A')))
        if(ch[i]>='A' and ch[i]<='z'):
            ch[i]=chr(ord(ch[i]) + ord('a')-ord('A'))
        resstr = "".join(ch)
        return resstr
print(convert("tHIS IS A EXAMPLE sENTENCE."))