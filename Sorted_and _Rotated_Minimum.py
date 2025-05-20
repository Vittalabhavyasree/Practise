def findMin(arr):
    n=len(arr)
    low=0
    high=n-1
    Min=float("inf")
    while(low<=high):
        mid=(low+high)//2
        if(arr[low]<=arr[mid]):
            if(arr[low]<Min):
                Min=arr[low]
            low=mid+1
        if(arr[mid]<=arr[high]):
            if(arr[mid]<Min):
                Min=arr[mid]
            high=mid-1
    return Min
arr=list(map(int,input().split()))
print(findMin(arr))