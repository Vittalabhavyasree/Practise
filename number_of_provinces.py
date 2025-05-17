def breadthFirstSearch(i,visited,q,adjList):
    while(q):
        node=q.pop(0)
        for it in adjList[node]:
            if(visited[it]==0):
                visited[it]=1
                q.append(it)
def numProvinces(adj,V):
    adjList=[]
    for i in range(V):
        adjList.append([])
    n=len(adj) #number of rows
    m=len(adj[0]) #number of columns
    for i in range(n):
        for j in range(m):
            if(adj[i][j]==1 and i!=j):
                adjList[i].append(j)
                adjList[j].append(i)
    visited=[0]*V
    c=0
    #i=0 only we cover connected components instead of for loop we use this line
    for i in range(0,V):
        if(visited[i]==0):
            visited[i]==1
            q=[i]
            breadFirstSearch(i,visited,q,adjList)
            c+=1
    return c
adj=list(map(int,input().split(",")))
V=int(input())
print(numProvinces(adj,V))