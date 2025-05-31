def dfs(sr,sc,image,visited,n,m,color,ele):
    visited=1
    image=[sr][sc]
    for r,c in [[-1,0],[1,0],[0,-1],[0,1]]:
        nrow=r+sr
        ncol=c+sc
        if(0<=nrow<n and 0<=ncol<n and not visited[nrow][ncol] and image[nrow][ncol]==ele):
            dfs(nrow,ncol,image,visited,n,m,color,ele)
def floodfill(image,sr,sc,color):
    n=len(image)
    m=len(image[0])
    visited=[]
    for i in range(n):
        temp=[0]*m
        visited.append(temp)
    ele=image[sr][sc]
    if(ele!=color):
        dfs(sr,sc,image,visited,n,m,color,ele)
    return image
