# INSERTION SORT : Takes an element places in correct position
def insertion(arr): # 14 9 15 6 8 12
    n=len(arr)
    for i in range(0,n):
        while(i>0 and arr[i-1]>arr[i]):
            arr[i-1],arr[i]=arr[i],arr[i-1]
            i-=1
    return arr
arr=list(map(int, input().split()))
print(insertion(arr))