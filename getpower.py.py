def getPower(x,n):
    if(n==0):
        return 1
    if(n%2==1):
        return x*getPower(x,n-1)
    return getPower(x*x,n//2)
def myPow(x,n):
    if(n<0):
        x=1/x
    n=abs(n)
    return getPower(x,n)

x = float(input())
n = int(input())
print(myPow(x, n))
