import sys
import heapq

sys.stdin = open('input.txt')

def dijkstra():
    heap = []
    heapq.heappush(heap, (0, 0))

    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = 1
            dist[v] = w
            for i in range(V+1):
                if not visited[i]:
                     heapq.heappush(heap, (dist[v]+G[v][i], i))
    return dist[V]

T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())
    G = [[11 for _ in range(V + 1)] for _ in range(V + 1)]
    dist = [11] * (V + 1)
    dist[0] = 0
    visited = [0] * (V + 1)
    for _ in range(E):
        start, end, w = map(int, input().split())
        G[start][end] = w

    print('#{} {}'.format(t, dijkstra()))