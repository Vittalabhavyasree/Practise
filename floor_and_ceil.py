# FLOOR : largest element in the array such that arr[id]<=x
# CEIL : smallest element in the array such that arr[ind]>=x , lower bound
def floor_and_ceil(a,n,x):
    def getFloor(a,n,x):
        low=0
        high=n-1
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            if(a[mid]<=x):
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
    def getCeil(a,n,x):
        low=0
        high=n-1
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            if(a[mid]>=x):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    floor=getFloor(a,n,x)
    ceil=getCeil(a,n,x)
    return [floor,ceil]
a=list(map(int, input().split()))
n=len(a)
x=int(input())
print(floor_and_ceil(a,n,x))