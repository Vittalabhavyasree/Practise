def searchRange(nums,k):
    def getLowerBound(nums,k):
        n=len(nums)
        low=0
        high=n-1
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            if(nums[mid]>=k):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    def getUpperBound(nums,k):
        n=len(nums)
        low=0
        high=n-1
        ans=n
        while(low<=high):
            mid=(low+high)//2
            if(nums[mid]>k):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    lb=getLowerBound(nums,k)
    if(lb==-1 or nums[lb]!=k):
        return [-1,-1]
    ub=getUpperBound(nums,k)-1
    return [lb,ub]
nums=list(map(int,input().split()))
k=int(input())
print(searchRange(nums,k))  