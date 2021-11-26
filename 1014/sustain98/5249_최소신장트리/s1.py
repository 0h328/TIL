# prim

import sys
sys.stdin = open('input.txt')
import heapq

t = int(input())
for idx in range(1, t+1):
    v, e = map(int, input().split())
    g = [[] for _ in range(v+1)]
    for _ in range(e):
        n1, n2, w = map(int, input().split())
        g[n1].append([w, n2])
        g[n2].append([w, n1])

    visited = [0] * (v + 1)
    visited[0] = 1
    candidate = g[0]
    heapq.heapify(candidate)
    total_weight = 0

    while candidate:
        w, e = heapq.heappop(candidate)
        if visited[e] == 0:
            visited[e] = 1
            total_weight += w
            for edge in g[e]:
                if visited[edge[1]] == 0:
                    heapq.heappush(candidate, edge)

    print('#{} {}'.format(idx, total_weight))







