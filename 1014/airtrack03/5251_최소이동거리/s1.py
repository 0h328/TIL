import heapq
import sys
sys.stdin = open('input.txt')

def dijkstra():
    heap = []
    heapq.heappush(heap, (0, 0))

    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = 1
            dist[v] = w
            for i in range(N+1):
                if not visited[i]:
                    heapq.heappush(heap, (dist[v] + graph[v][i], i))

    return dist[N]


T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())

    graph = [[11] * (N+1) for _ in range(N+1)]
    dist = [10000001] * (N+1)
    dist[0] = 0
    visited = [0] * (N+1)

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w

    ans = dijkstra()

    print('#{} {}'.format(tc, ans))