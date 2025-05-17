'''def longestSubarray(arr,k):
    n=len(arr)
    ans=[]
    for i in range(0,n):
        for j in range(i,n):
            ans.append(arr[i:j+1])
    maxLen=0
    for lst in ans:
        if(sum(lst)==k):
            if(len(lst)>maxLen):
                maxLen=len(lst)
    return maxLen
arr=list(map(int,input().split()))
k=int(input())
print(longestSubarray(arr,k))'''
#hashing technique
def longestSubarray(arr,k):
    d={}
    sum=0
    maxLen=0
    n=len(arr)
    for i in range(0,n):
        sum+=arr[i]
        if(sum==k):
            maxLen=i+1
        rem=sum-k
        if(rem in d):
            maxLen=max(maxLen,i-d[rem])
        if(sum not in d):
            d[sum]=i
    return maxLen
arr=list(map(int,input().split()))
k=int(input())
print(longestSubarray(arr,k))