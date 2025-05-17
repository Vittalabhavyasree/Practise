# find the missing number in a given list
'''def missing(L):
    n=len(L)+1
    res=n*(n+1)//2
    return res-sum(L)
L=list(map(int, input().split(",")))
print(missing(L)) '''

# print zero in last
'''def zeros(n):
    s=0
    for i in range(len(n)):
        if n[i]!=0:
            n[s]=n[i]
            if s!=i:
                n[i]==0
            s+=1
    return n
n=list(map(int, input().split()))
res=zeros(n)
print(res)'''
# another method
'''a=list(map(int, input().split()))
for i in a:
    if i==0:
        a.remove(0)
        a.append(0)
print(a)'''

# print even in last 2 pointer
'''l=list(map(int, input().split()))
k=0
for i in range(len(l)):
    if l[i]%2!=0:
        temp=l.pop(i)
        l.insert(k,temp)
        k+=1
print(l)'''
