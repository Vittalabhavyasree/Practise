def printGraph(V,e,edges):
    adjList=[]
    for i in range(V):
        adjList.append([])
    for n,m in edges:
        adjList[n].append(m) 
        adjList[m].append(n)
    for lst in adjList:
        lst.sort()
    return adjList
V=int(input())
e=int(input())
edges=[]
for i in range(e):
    lst=list(map(int,input().split()))
    edges.append(lst)
print(printGraph(V,e,edges))