import sys
from heapq import heappush, heappop
sys.stdin = open('input.txt')
input = sys.stdin.readline
INF = sys.maxsize
print(INF)

def dijkstra(start):
    heap = []
    heappush(heap, (0, start))

    while heap:
        w, s = heappop(heap)
        if dist[s] < w:
            continue
        for node, weight in G[s]:
            if w + weight < dist[node]:
                dist[node] = w + weight
                heappush(heap, (dist[node], node))
    return dist

V, E = map(int, input().split())
K = int(input())
G = [[] for _ in range(V+1)]
dist = [INF] * (V+1)
dist[K] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))

dijkstra(K)
for i in range(1, V+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])


