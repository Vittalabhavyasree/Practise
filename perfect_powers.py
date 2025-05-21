# T.C.= O(N)
'''
def nthRoot(n,m):
    ans=-1
    for i in range(1,m+1):
        if(i**n==m):
            return i
        elif(i**n>m):
            break
    return ans
n=int(input())
m=int(input())
print(nthRoot(n,m))
'''
# another way    
# T.C = O(N)
'''
def nthRoot(n,m):
    ans=-1
    for i in range(1,m+1):
        if(i**n==m):
            ans=i
            break
        elif(i**n>m):
            break
    return ans
n=int(input())
m=int(input())
print(nthRoot(n,m))
'''

# By using binary search
# T.C = O(logN)
def nthRoot(n,m):   
    low=1
    high=m
    ans=-1
    while(low<=high):
        mid=(low+high)//2
        if(mid**n==m):
            return mid
        elif(mid**n>m):
            high=mid-1
        else:
            low=mid+1
    return ans
n=int(input())
m=int(input())
print(nthRoot(n,m))