'''def findPages(arr,n,m):
    def canWeAllocate(maxPages,arr):
        no_of_pages_allocated=arr[0]
        students=1
        for pages in range(1,len(arr)):
            if(arr[pages]+no_of_pages_allocated<=maxPages):
                no_of_pages_allocated+=arr[pages]
            else:
                no_of_pages_allocated=arr[pages]
                students+=1
        return students
    if(m>len(arr)):
        return -1
    Min=max(arr)
    Max=sum(arr)
    for maxPages in range(Min,Max+1):
        if(canWeAllocate(maxPages,arr)<=m):
            return maxPages
arr=list(map(int, input().split()))
n=int(input())
m=int(input())
print(findPages(arr,n,m))
'''

# Binary search method
def findPages(arr,n,m):
    def canWeAllocate(maxPages,arr):
        no_of_pages_allocated=arr[0]
        students=1
        for pages in range(1,len(arr)):
            if(arr[pages]+no_of_pages_allocated<=maxPages):
                no_of_pages_allocated+=arr[pages]
            else:
                no_of_pages_allocated=arr[pages]
                students+=1
        return students
    if(m>len(arr)):
        return -1
    low=max(arr)
    high=sum(arr)
    while(low<=high):
        maxPages=(low+high)//2
        if(canWeAllocate(maxPages,arr)<=m):
            high=maxPages-1
        else:
            low=maxPages+1
    return low
arr=list(map(int, input().split()))
n=int(input())
m=int(input())
print(findPages(arr,n,m))