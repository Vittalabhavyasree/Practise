arr=list(map(int,input().split()))
n=len(arr)
Sum=0
for i in range(0,n):
    for j in range(i,n):
        Sum+=sum(arr[i:j+1])
print(Sum)