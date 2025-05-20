def search_duplicates(arr,k):
    n=len(arr)
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==k):
            return True
        if(arr[low]==arr[mid]==arr[high]):
            low+=1
            high-=1
        elif(arr[low]<=arr[mid]):
            if(arr[low]<=k<=arr[mid]):
                high=mid-1
            else:
                low=mid+1
        elif(arr[mid]<=arr[high]):
            if(arr[mid]<=k<arr[high]):
                low=mid+1
            else:
                high=mid-1
    return False        
arr=list(map(int,input().split()))
k=int(input())
print(search_duplicates(arr,k))