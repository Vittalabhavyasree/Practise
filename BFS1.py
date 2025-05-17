def breadthFirstSearch(i,visited,q,adj,ans):
    while(q):
        node=q.pop(0)
        for it in adj[node]:
            if(visited[it]==0):
                visited[it]=1
                q.append(it)
        ans.append(node)
def bfs(adj):
    v=len(adj)
    ans=[]
    visited=[0]*v
    i=0 # for connected graph
   # for i in range(0,v): #loop is for unconnected components
    if (visited[i]==0):
        visited[i]=1
        q=[i]
        breathFirstSearch(i,visited,q,adj,ans)
    return ans
adj=list(map(int,input().split()))
print(bfs(adj))