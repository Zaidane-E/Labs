def histo(tup):
    dic={}
    for i in tup:
        dic[i]=dic.get(i,0)+1
    return dic
tup=(1,2,2,3,3,3,4,4,4,4,5,5,5,5,5)
lst=list(histo(tup).items())
lst.sort()
print(lst)
