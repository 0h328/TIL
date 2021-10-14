import sys
import heapq
sys.stdin = open('input.txt')


def dijkstra():
    heap = []
    heapq.heappush(heap, (0, 0))

    while heap:
        w, n = heapq.heappop(heap)
        if not visited[n]:
            visited[n] = 1
            dist[n] = w
            for i in range(N+1):
                if not visited[i]:
                    heapq.heappush(heap, (dist[n]+G[n][i], i))
    return dist[n]


T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    G = [[1e10 for _ in range(N+1)] for _ in range(N+1)]
    dist = [1e10] * (N+1)
    dist[0] = 0
    visited = [0] * (N+1)
    
    for _ in range(E):
        start, end, w = map(int, input().split())
        G[start][end] = w
    
    answer = dijkstra()

    print('#{} {}'.format(tc, answer))