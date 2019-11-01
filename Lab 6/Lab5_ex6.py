def coder(s):
    a=[]
    for i in range(0,len(s)-1,2):
        a.append(s[i+1])
        a.append(s[i])
    if len(s)%2!=0:
        a.append(s[-1])
    return ''.join(a)
s=input("Entrez un message à coder: ")
print(coder(s))
