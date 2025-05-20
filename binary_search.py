def binary(arr,k):   #T.C = O(logN)
    n=len(arr)
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==k):
            return mid
        elif(k>arr[mid]):
            low=mid+1
        elif(k<arr[mid]):
            high=mid-1
    return -1
arr=list(map(int, input().split()))
k=int(input())
print(binary(arr,k))
