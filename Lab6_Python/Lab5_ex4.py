def compte(s,a):
    return s.count(a)

def compte2(s,a):
    c=0
    for i in range(len(s)):
        if s[i]==a:
            c=c+1
        i=i+1
    return c
s=input("Entrez une chaine de caracteres: ")
print(compte(s,'a'))
print(comtpe(s,'de la'))
