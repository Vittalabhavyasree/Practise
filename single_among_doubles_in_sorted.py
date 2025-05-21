'''
def single(arr):
    d={}
    for i in arr:
        if(i in d):
            d[i]=d[i]+1
        else:
            d[i]=1
        for key,value in d.items():
            if(value==1):
                return key
arr=list(map(int,input().split()))
print(single(arr))
'''

# another method with binary search

def find(arr):
    n=len(arr)
    if(n==1):
        return arr[0]
    elif(arr[0]!=arr[1]):
        return arr[0]
    elif(arr[n-1]!=arr[n-2]):
        return arr[n-1]
    low=1
    high=n-2
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid+1]):
            return arr[mid]
        # you are on the left half
        elif(mid%2==1 and arr[mid]==arr[mid-1] or (mid%2==0 and arr[mid]==arr[mid+1])):
            low=mid+1
        # you are on the right half
        elif(mid%2==0 and arr[mid]==arr[mid-1] or (mid%2==1 and arr[mid]==arr[mid+1])):
            high=mid-1
arr=list(map(int,input().split()))
print(find(arr))
