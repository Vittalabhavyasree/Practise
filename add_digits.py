def addDigits(n):    
    while(n>=10):
        Sum=0
        while(n>0):
            rem=n%10
            Sum+=rem
            n=n//10
        n=Sum
    return n
n=int(input())
print(addDigits(n))