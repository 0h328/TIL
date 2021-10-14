import sys
from heapq import *
sys.stdin = open('input.txt', 'r')

T = int(input())


def dijkstra(start):
    heap = []
    heappush(heap, (0, start))

    while heap:
        dist, node = heappop(heap)

        for next_dist, next_node in graph[node]:
            total_dist = dist + next_dist
            if distance[next_node] > total_dist:
                distance[next_node] = total_dist
                heappush(heap, (total_dist, next_node))


for tc in range(1, T + 1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))

    # 최선의 선택을 위해 가장 가중치가 작은 간선부터 확인
    for g in graph:
        g.sort()

    INF = 1e9
    distance = [INF] * (N + 1)
    distance[0] = 0
    dijkstra(0)

    print('#{} {}'.format(tc, distance[N]))


