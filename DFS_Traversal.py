def depthFirstSearch(i,visited,adj,ans):
    visited[i]=1
    ans.append(i)
    for it in adj[i]:
        if (visited[it]==0):
            depthFirstSearch(it,visited,adj,ans)
def dfs(adj):
    v=len(adj)
    visited=[0]*v
    ans=[]
    for i in range(0,v):
        if(visited[i]==0):
            depthFirstSearch(i,visited,adj,ans)
    return ans
adj=list(map(int,input().split(",")))
print(dfs(adj))