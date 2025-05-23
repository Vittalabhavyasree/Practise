'''
n=int(input())
if(n<=1):
    print("not prime")
else:
    flag=True
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            flag=False
            break
    if(flag==True):
        print("prime")        
    else:
        print("not prime")'''

# another way for printing factors of a number
'''
n=int(input())
for i in range(1,n+1):
    if(n%i==0):
        print(i)
'''
# another way
'''n=int(input())
c=0
for i in range(1,n+1):
    if(n%i==0):
        c+=1
if(c==2):
    print("prime")
else:
    print("not a prime")
'''
# another way
'''def isPrime(num):
    c=0
    for num in range(1,n+1):
        if(n%num==0):
            c+=1
    return c==2
n=int(input())
count=0
for num in range(2,n):
    if(isPrime(num)):
        count+=1
print(count)'''

# another optimal way by seive of eratosthenes method
'''n=int(input())
prime=[1]*n
for i in range(2,n):
    if(prime[i]==1):
        for j in range(2*i,n,i):
            prime[j]=0
count=0
for i in range(2,n):
    if(prime[i]==1):
        count+=1
print(count)'''

# optimise
'''n=int(input())
prime=[1]*n
for i in range(2,n):
    if(prime[i]==1):
        for j in range(i*i,n,i):
            prime[j]=0
count=0
for i in range(2,n):
    if(prime[i]==1):
        count+=1
print(count)'''

n=int(input())  # T.C = O(N.log(logN)) = O(1)
prime=[1]*n
for i in range(2,int(n**0.5)+1):
    if(prime[i]==1):
        for j in range(i*i,n,i):
            prime[j]=0
count=0
for i in range(2,n):   # T.C = O(N)
    if(prime[i]==1):
        count+=1
print(count)
