'''def fibo(n): # t.c = O(2*n)
    if(n<=1): # s.c = O(n)
        return n
    return fibo(n-1)+fibo(n-2)
n=int(input())
print(fibo(n))'''
#another method with dp
'''def fibo(n,dp): # T.C = O(n)
    if(n<=1):  # S.C = O(n)+O(n)
        return n
    if(dp[n]==-1):
        dp[n]=fibo(n-1,dp)+fibo(n-2,dp)
    return dp[n]
n=int(input())
dp=[-1]*(n+1)
print(fibo(n,dp))'''
#another method dp without recurrsion
'''def fibo(n,dp): # T.C = O(n)
    if(n==0 or n==1): # S.C = O(n)
        return n
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
n=int(input()) 
dp=[-1]*(n+1)
print(fibo(n,dp))'''
# without using dp array
def fibo(n): # T.C = O(n)
    prev2=0
    prev1=1
    for i in range(2,n+1):
        curr=prev2+prev1
        prev2=prev1
        prev1=curr
    return prev1
n=int(input())
print(fibo(n))