# BUBBLE SORT : Push the max elements to the last by adjacent swapping
def bubblesort(arr):    # T.C = O(N^2)
    n=len(arr)
    for i in range(n-1,-1,-1):
        for j in range(i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=list(map(int, input().split()))
print(bubblesort(arr))

# another simple way to solve testcases
'''
def bubblesort(arr):
    arr.sort()
    return arr
arr=list(map(int, input().split()))
print(bubblesort(arr))
'''