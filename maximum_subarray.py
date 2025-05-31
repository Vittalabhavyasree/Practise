'''def subarray(nums):
    n=len(nums)
    maxSum=float("-inf")
    for i in range(0,n):
        for j in range(i,n):
            Sum=sum(nums[i:j+1])
            maxSum=max(maxSum,Sum)
    return maxSum
nums=list(map(int, input().split(",")))
print(subarray(nums))'''

# KADANES ALGORITHM
def subarray(nums):
    n=len(nums)
    maxSum=float("-inf")
    currentSum=0
    for i in nums:
        currentSum+=i
        maxSum=max(maxSum,currentSum)
        if(currentSum<0):
            currentSum=0
    return maxSum
nums=list(map(int, input().split(",")))
print(subarray(nums))   
