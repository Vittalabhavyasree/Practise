# count the no. of digits in a number using recurrsion
'''
def count(n):
    if n == 0:
        return 0
    return 1 + count(n//10)
n=int(input()) 
print(count(n)) 
'''
# another method
'''
def fun(n):
    if n//10==0:
        return 1
    return 1+fun(n//10)
n=int(input())
print(fun(n))
'''

# printing the sum of digits in a number
'''
def sum(n):
    s=0
    while n>0:
        digit = n%10
        s+=digit
        n=n//10
    return s
n=int(input())
print(sum(n))
'''

# printing the sum of digits in a number by using recurrsion
'''
def fun(n):
    if n//10==0:
        return n
    return n % 10 + fun(n//10)
n=int(input())
print(fun(n))
'''

# find the minimum number in a list
'''
def fun(nums):
    def rec(nums,i):
        if i ==len(nums)-1:
            return nums[i]
        min=rec(nums,i+1)
        return min if min<nums[i] else nums[i]  
    return rec(nums,i)
nums=list(map(int, input().split(",")))
i=int(input())
print(fun(nums))
'''

# find the maximum number in a list
'''
def fun(nums):
    def rec(nums,i):
        if i ==len(nums)-1:
            return nums[i]
        min=rec(nums,i+1)
        return min if min>nums[i] else nums[i]
    return rec(nums,i)
nums=list(map(int, input().split(",")))
i=int(input())
print(fun(nums))
'''

# find the min max numbers in a list
'''
def fun(nums):
    def rec(nums,i):
        if i == len(nums)-1:
            return nums[i], nums[i]
        min , max=rec(nums,i+1)
        min = min if min<nums[i] else nums[i]
        max = max if max>nums[i] else nums[i]
        return min , max
    return rec(nums,i)
nums=list(map(int, input().split(",")))
i=int(input())
min , max = fun(nums)
print(min , max) 
'''