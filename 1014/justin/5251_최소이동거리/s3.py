def dijkstra():
    heap = []
    heapq.heappush(heap, (0, 0))                                # heap에 들어가는 순서 -> (가중치, 정점)
    while heap:
        w, v = heapq.heappop(heap)                              # 가중치, 정점 (최솟값 반환)

        if not visited[v]:                                      # 아직 방문하지 않았다면
            visited[v] = 1                                      # 방문처리
            dist[v] = w                                         # v 정점의 가중치 갱신

            for i in range(V+1):
                """
                 - 우선순위 큐를 활용한 경우 dist[i] > dist[v] + G[v][i] 조건 불필요
                 - min_heap은 항상 가장 작은 값이 루트에 존재 -> 방문하지 않은 경우만 처리하기 때문에 다른 값들이 들어있다고 해도 어차피 수행하지 않을 것
                """
                # if not visited[i] and dist[i] > dist[v] + G[v][i]
                if not visited[i]:
                     heapq.heappush(heap, (dist[v]+G[v][i], i))  # 가중치, 정점
    return dist[V]

import sys
import heapq
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[987654321 for _ in range(V+1)] for _ in range(V+1)]
    dist = [987654321] * (V+1)
    dist[0] = 0
    visited = [0] * (V+1)
    for _ in range(E):
        start, end, w = map(int, input().split())
        G[start][end] = w
    ans = dijkstra()
    print('#{} {}'.format(tc, ans))