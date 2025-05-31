# printing a right-angled triangle pattern 
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# printing a right-angled triangle pattern with numbers
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# printing an inverted right-angled triangle pattern
n=int(input())  
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# printing a sqaure pattern
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()

# printing a hollow square pattern
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# printing a diamond pattern
n=int(input())
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print()
# printing an inverted diamond pattern
n=int(input())
for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print()

# printing a hollow pyramid pattern
n=int(input())
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
        if j==1 or j==2*i-1 or i==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# printing a right-angled triangle pattern with numbers in reverse order
n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# printing a right-angled triangle pattern with numbers in reverse order and spaces
n=int(input())
for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
