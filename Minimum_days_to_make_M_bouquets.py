# linear solution
'''def bouquets(m,k,arr):
    if(m>len(arr)):
        return -1
    Min=min(arr)
    Max=max(arr)
    for bloomday in range(Min,Max+1):
        count=0
        noOfB=0
        for flower in arr:
            if(flower<=bloomday):
                count+=1
            else:
                noOfB+=count//k
                count=0
        noOfB+=count//k
        if(noOfB>=m):
            return bloomday
    return -1
m=int(input())
k=int(input())
arr=list(map(int, input().split()))
print(bouquets(m,k,arr))
'''
# binary search logic
def bouquets(m,k,arr):
    if(m>len(arr)):
        return -1
    low=min(arr)
    high=max(arr)
    ans=-1
    for bloomday in range(low,high+1):
        count=0
        noOfB=0
        for flower in arr:
            if(flower<=bloomday):
                count+=1
            else:
                noOfB+=count//k
                count=0
        noOfB+=count//k
        if(noOfB<m):
            low=bloomday+1
        else:
            ans=bloomday
            high=bloomday-1   
    return ans
m=int(input())
k=int(input())
arr=list(map(int, input().split()))
print(bouquets(m,k,arr))