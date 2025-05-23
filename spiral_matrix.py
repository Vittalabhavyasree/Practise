def spiralOrder(matrix):
    n=len(matrix)
    m=len(matrix[0])
    sr=0
    er=n-1
    sc=0
    ec=m-1
    res=[]
    while(sr<=er and sc<=ec):
        for i in range(sc,ec+1):
            res.append(matrix[sr][i])
        sr+=1
        for i in range(sr,er+1):
            res.append(matrix[i][ec])
        ec-=1
        if(sr<=er):
            for i in range(ec,sc-1,-1):
                res.append(matrix[er][i])
            er-=1
        if(sc<=ec):
            for i in range(er,sr-1,-1):
                res.append(matrix[i][sc])
            sc+=1
    return res
matrix=list(map(int, input().split()))
print(spiralOrder(matrix))