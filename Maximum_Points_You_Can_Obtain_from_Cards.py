def maxScore(arr,k):
    n=len(arr)
    left=0
    right=k-1
    leftSum=sum(arr[left:right+1])
    rightSum=0
    maxSum=leftSum
    rightIndex=n-1
    for i in range(k-1,-1,-1):
        leftSum-=arr[i]
        rightSum+=arr[rightIndex]
        maxSum=max(maxSum,leftSum+rightSum)
        rightIndex-=1
    return maxSum
arr=list(map(int, input().split()))
k=int(input())
print(maxScore(arr,k))