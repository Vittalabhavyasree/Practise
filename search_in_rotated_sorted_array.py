# Two rules : 
# 1. Identify the sorted half.
# 2. Check whether elements exist in sorted half.
def search(arr,k):
    n=len(arr)
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==k):
            return mid
        # left half is sorted
        elif(arr[low]<=arr[mid]):
            if(arr[low]<=k<=arr[mid]):
                high=mid-1
            else:
                low=mid+1
        # right half is sorted or not
        elif(arr[mid]<-arr[high]):
            if(arr[mid]<=k<=arr[high]):
                low=mid+1
            else:
                high=mid-1
    return -1
arr=list(map(int,input().split()))
k=int(input())
print(search(arr,k))