# CONSTANT WINDOW
# to generate max sum of subarray with given lengthof subarray
'''arr=list(map(int,input().split()))       # T.C = O(N^2)
k=int(input())
n=len(arr)
maxSum=0
for i in range(0,n):
    for j in range(i,n):
        if(len(arr[i:j+1])==k):
            maxSum=max(maxSum,sum(arr[i:j+1]))
print(maxSum)'''

# Another method OPTIMMAL METHOD
arr=list(map(int, input().split()))
k=int(input())
n=len(arr)
left=0
right=k-1
Sum=sum(arr[left:right+1])
maxSum=Sum
while(right<n-1):
    Sum-=arr[left]
    left+=1
    right+=1
    Sum+=arr[right]
    maxSum=max(maxSum,Sum)
print(maxSum)