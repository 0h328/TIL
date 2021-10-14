import sys
import heapq
sys.stdin=open('input.txt')

def dijkstra():
    heap=[]
    heapq.heappush(heap,(0,0))

    while heap:
        w,v = heapq.heappop(heap)
        if not visited[v]:
            visited[v]=1
            dist[v]=w
            for i in range(V+1):
                if not visited[i]:
                    heapq.heappush(heap,(dist[v]+G[v][i],i))
    return dist[V]

for test in range(1,1+int(input())):
    V,E = map(int,input().split())
    G = [[1e9 for _ in range(V+1)] for _ in range(V+1)]
    dist = [1e9]*(V+1)
    dist[0]=0
    visited=[0]*(V+1)

    for _ in range(E):
        start,end,w = map(int,input().split())
        G[start][end]=w
    answer = dijkstra()

    print('#{} {}'.format(test, answer))
