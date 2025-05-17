def check(ind,arr,k):
    if(k==0):
        return 1
    if(k<0 or ind==len(arr)):
        return 0
    path1=check(ind+1,arr,k-arr[ind])
    path2=check(ind+1,arr,k)
    return path1+path2

k=int(input())
arr=list(map(int,input().split()))

ind=0
print(check(ind,arr,k))
