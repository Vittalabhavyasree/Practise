# By using two pointers
'''
nums1=list(map(int, input().split()))
nums2=list(map(int, input().split()))
i=0
j=0
result=[]
while(i<len(nums1) and j<len(nums2)):
    if(nums1[i]<=nums2[j]):
        result.append(nums1[i])
        i+=1
    else:
        result.append(nums2[j])
        j+=1
while(i<len(nums1)):
    result.append(nums1[i])
    i+=1
while(j<len(nums2)):
    result.append(nums2[j])
    j+=1
print(result)
'''

# By using function
def ms(nums,n):      # T.C = O(NlogN)
    def mergeSort(nums,low,high):   # S.C = O(N)
        if(low>=high):
            return
        mid=(low+high)//2 
        mergeSort(nums,low,mid)
        mergeSort(nums,mid+1,high)
        Sort(nums,low,mid,high)
    def Sort(nums,low,mid,high):
        i=low
        j=mid+1
        res=[]
        while(i<=mid and j<=high):
            if(nums[i]<=nums[j]):
                res.append(nums[i])
                i+=1
            else:
                res.append(nums[j])
                j+=1
        while(i<=mid):
            res.append(nums[i])
            i+=1
        while(j<=high):
            res.append(nums[j])
            j+=1
        for ind,val in enumerate(res):
            nums[ind+low]=val 
    low=0
    high=n-1
    mergeSort(nums,low,high)
    return nums
nums=list(map(int,input().split()))
n=len(nums)
print(ms(nums,n))