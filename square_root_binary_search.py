'''
def floorSqrt(n):
    ans=0
    for i in range(1,n+1):
        if(i*i<=n):
            ans=i
        else:
            break
    return ans
n=int(input())
print(floorSqrt(n))
'''

# By using binary search
def floorSqrt(n):
    ans=0
    low=1
    high=n
    while(low<=high):
        mid=(low+high)//2
        if(mid*mid<=n):
            ans=mid
            low=mid+1
        elif(mid*mid>=n):
            high=mid-1
    return ans
n=int(input())
print(floorSqrt(n))

# another method without taking ans
def floorSqrt(n):
    low=1
    high=n
    while(low<=high):
        mid=(low+high)//2
        if(mid*mid<=n):
            ans=mid
            low=mid+1
        elif(mid*mid>=n):
            high=mid-1
    return high
n=int(input())
print(floorSqrt(n))