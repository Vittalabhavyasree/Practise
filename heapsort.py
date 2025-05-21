def max_heap(arr,n,i):
    root=i
    left=2*i+1
    right=2*i+2
    if left<n and arr[left]>arr[root]:
        root=left
    if 
    
def heapsort(arr):
    n=len(arr)
    for i in range(n//2,-1,-1):
        max_heap(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        max_heap(arr,i,0)
        
        
arr=[10,1,6,4,11,13,2]
