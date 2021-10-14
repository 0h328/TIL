import sys
from heapq import *
sys.stdin = open('input.txt', 'r')

T = int(input())


# 1. prim을 이용한 풀이
def prim(start):
    mst = 0
    connected = set()
    connected.add(start)
    candidates = graph[start]
    heapify(candidates)

    while candidates:
        weight, node1, node2 = heappop(candidates)
        if node2 not in connected:
            connected.add(node2)
            mst += weight

            for edge in graph[node2]:
                if edge not in connected:
                    heappush(candidates, edge)

    return mst


for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1].append((w, n1, n2))
        graph[n2].append((w, n2, n1))

    print('#{} {}'.format(tc, prim(1)))
