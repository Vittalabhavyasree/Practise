# LOWER BOUND : Smallest element in the array such that arr[ind]>=x
def lowerbound(arr,k):
    n=len(arr)
    low=0
    high=n-1
    ans= n
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>=k):
            ans=mid
            high=mid-1
        else: 
            low=mid+1
    return ans
arr=list(map(int, input().split()))
k=int(input())
print(lowerbound(arr,k))