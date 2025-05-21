# linear solution
'''from math import *
def divisor(arr,k):
    for div in range(1,max(arr)+1):
        Sum=0
        for num in arr:
            Sum+=ceil(num/div)
        if(Sum <=k):
            return div
arr=list(map(int, input().split()))
k=int(input())
print(divisor(arr,k))
'''
# Binary search logic
from math import * 
def divisor(arr,k):
    low=1
    high=max(arr)
    while(low<=high):
        div=(low+high)//2
        Sum=0
        for num in arr:
            Sum+=ceil(num/div)
        if(Sum<=k):
            high=div-1
        else:
            low=div+1
    return low
arr=list(map(int, input().split()))
k=int(input())
print(divisor(arr,k))