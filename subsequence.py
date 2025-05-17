def check(ind,arr,k):
    if(k==0):
        return True
    if(k<0 or ind==len(arr)):
        return False
    path1=check(ind+1,arr,k-arr[ind])
    if(path1==True):
        return True
    path2=check(ind+1,arr,k)
    return path1 or path2
def checkSubsequenceSum(N,arr,k):
    ind=0
    return check(ind,arr,k)
N = int(input())
arr = list(map(int, input().split()))
k = int(input())
print(checkSubsequenceSum(N,arr,k))
