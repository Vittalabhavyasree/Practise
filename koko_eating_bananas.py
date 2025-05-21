#linear solution
''' 
from math import *
def koko(arr,k):
    for noOfBanana in range(1,max(arr)+1):
        time=0
        for num in arr:
            time+=ceil(num/noOfBanana)
        if(time<=k):
            return noOfBanana
arr=list(map(int, input().split()))
k=int(input())
print(koko(arr,k))
'''
# Binary search logic
from math import *
def koko(arr,k):
    low=1
    high=max(arr)
    while(low<=high):
        noOfBanana=(low+high)//2
        time=0
        for num in arr:
            time+=ceil(num/noOfBanana)
        if(time<=k):
            high=noOfBanana-1
        else:
            low=noOfBanana+1
    return low
arr=list(map(int, input().split()))
k=int(input())
print(koko(arr,k)) 