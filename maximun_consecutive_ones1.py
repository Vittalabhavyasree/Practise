def findMaxConsecutiveOnes(nums):
    n=len(nums)
    left=0
    right=0
    maxLen=0
    count=0
    while(right<n):
        if(nums[right]==1):
            count+=1 
            maxLen=max(maxLen,right-left+1)
            right+=1
        else:
            right+=1
            left=right
    return maxLen
nums=list(map(int,input().split()))
print(findMaxConsecutiveOnes(nums))           
        