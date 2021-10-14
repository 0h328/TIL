import sys
sys.stdin = open('input.txt')
import heapq


t = int(input())
INF = int(1e9)
for idx in range(1, t+1):
    n, e = map(int, input().split())
    g = [[] for _ in range(n+1)]
    for _ in range(e):
        s, e, w = map(int, input().split())
        g[s].append((w, e))

    visited = [0]*(n+1)
    weight = [INF]*(n+1)
    q = []
    heapq.heappush(q, (0, 0))
    weight[0] = 0
    while q:
        w, x = heapq.heappop(q)
        visited[x] = 1
        for nw, e in g[x]:
            if visited[e] == 0 and weight[e] > w + nw:
                weight[e] = w + nw
                heapq.heappush(q, (weight[e], e))

    print('#{} {}'.format(idx, weight[-1]))


