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
        print("not prime")