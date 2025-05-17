import heapq
def dijkstra(v,edges,src):
    adjList=[]
    for i in range(v):
        adjList.append([])
    for n,m,w in edges:
        adjList[n].append((m,w))
        adjList[m].append((n,w))
    distance=[float("inf")]*v 
    pq=[]
    distance[src]=0
    heapq.heappush(pq,(0,src))
    while(pq):
        dist,node=heapq.heappop(pq)
        for adjNode,adjDist in adjList[node]:
            if(dist+adjDist<distance[adjNode]):
                distance[adjNode]=dist+adjDist
                heapq.heappush(pq,(dist+adjDist,adjNode))
    return distance
v=int(input())
src=int(input())
edges=eval(input("enter edges as a list of[u,v,w]:"))
print(dijkstra(v,edges,src))