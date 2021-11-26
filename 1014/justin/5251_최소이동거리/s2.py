"""
- 어떤 경로를 통해서 이 최소 거리가 나온지는 알 수 없지만
- 결과적으로 최소 얼마의 비용이면 이곳에 올 수 있는지는 알 수 있음
"""
def get_min_idx():
    min_val = 999999
    min_idx = 0
    for i in range(N+1):                            # 방문 안 한 노드 중 dist가 최소인 노드 찾기
        if not visited[i] and dist[i] < min_val:
            min_idx = i
            min_val = dist[i]
    return min_idx

def dijkstra(goal):
    dist[0] = 0                                              # 출발점의 가중치
    for i in range(N+1):
        if G[0][i]:                                          # 출발점과 인접한 정점이라면
            dist[i] = G[0][i]                                # dist 초기화
    visited[0] = 1                                           # 시작노드

    while True:
        vertex = get_min_idx()
        visited[vertex] = 1                                  # dist가 가장 작은 노드 방문처리
        if vertex == goal:                                   # 도착지에 도착하면
            return dist[goal]                                # 거리 반환
        for i in range(N+1):
            if G[vertex][i]:                                 # min_idx에 인접인 노드에 대해
                if dist[i] > dist[vertex] + G[vertex][i]:    # min_idx를 경유하는 비용이 더 작으면
                    dist[i] = dist[vertex] + G[vertex][i]    # dist[i]를 더 적은 값(경유하는 경로의 비용)으로 갱신

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    G = [[0 for _ in range(N+1)] for _ in range(N+1)]      # 그래프 초기화
    visited = [0] * (N+1)                                  # 정점 방문 여부
    dist = [987654321] * (N+1)                             # 0번 부터의 거리(가중치)

    for _ in range(E):
        start, end, w = map(int, input().split())
        G[start][end] = w                                  # 방향 그래프
    ans = dijkstra(N)
    print('#{} {}'.format(tc, ans))