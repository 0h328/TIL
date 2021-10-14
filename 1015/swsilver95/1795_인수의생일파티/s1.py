from heapq import *
import sys
sys.stdin = open('input.txt', 'r')


def dijkstra(start, distance):
    heap = []
    heappush(heap, (0, start))

    while heap:
        dist, node = heappop(heap)

        for next_dist, next_node in graph[node]:
            total_dist = dist + next_dist
            if distance[next_node] > total_dist:
                distance[next_node] = total_dist
                heappush(heap, (total_dist, next_node))

    return distance


T = int(input())

for tc in range(1, T + 1):
    N, M, X = map(int, input().split())     # N: 집 번호 / M: 간선의 수 / X: 목표 집(시작 지점)
    graph = [[] for _ in range(N + 1)]
    INF = 1e9
    distance_original = [INF] * (N + 1)
    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x].append((c, y))

    for g in graph:
        g.sort()

    main_distance = distance_original[:]
    main_distance[X] = 0
    main_distance = dijkstra(X, main_distance)

    max_node = (0, 0)
    for i in range(1, N + 1):
        dist = distance_original[:]
        dist[0] = 0
        dist[i] = 0
        tmp = dijkstra(i, dist)
        tmp_dist = tmp[X] + main_distance[i]
        if max_node[0] < tmp_dist:
            max_node = (tmp_dist, i)

    # print(main_distance)
    max_time = max_node[0]
    print('#{} {}'.format(tc, max_time))