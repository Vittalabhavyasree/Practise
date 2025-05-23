def search(matrix,target):
    n=len(matrix)
    m=len(matrix[0])
    row=0
    col=m-1
    while(row<n and col>=0):
        if(matrix[row][col]==target):
            return True
        elif(target>matrix[row][col]):
            row+=1
        elif(target<matrix[row][col]):
            col-=1
    return False
matrix=list(map(int,input().split()))
target=int(input())
print(search(matrix,target))