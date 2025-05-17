def unique(L):
    list=[]
    for i in L:
        if L.count(i) == 1:
            list.append(i)
    return list
L=list(map(int, input().split(",")))
print(unique(L))