def get_min_idx(dist, visit):
    min_index = 0
    for i in range(1, N+1):                              # 방문 안한 노드 중에 dist가 최소인 노드 찾기
        if visit[i] == 0 and dist[i] < dist[min_index]:
            min_index = i
    return min_index


def dijkstra(X, adj, dist):
    dist[X] = 0                                          # 출발점의 가중치

    for i in range(1, N+1):                              # 출발지로부터의 비용
        if adj[X][i]:                                    # 출발점과 인접한 노드
            dist[i] = adj[X][i]

    visited = [0] * (N+1)                                # 방문처리
    visited[X] = 1

    for _ in range(N-1):                                 # 출발지 제외한 가중치 구하기
        node = get_min_idx(dist, visited)
        visited[node] = 1                                # dist 가장 작은 노드 방문처리

        for i in range(1, N+1):
            if adj[node][i] and visited[i] == 0:         # min_index 인접노드에 대해서
                if dist[i] > dist[node] + adj[node][i]:  # min_index를 경우하는 비용이 더 작으면
                    dist[i] = dist[node] + adj[node][i]  # dist[x] 갱신

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())         # 정점, 간선
    G1 = [[0] * (N+1) for _ in range(N+1)]      # 진출기준
    G2 = [[0] * (N+1) for _ in range(N+1)]      # 진입기준
    dist1 = [987654321] * (N+1)                 # 가중치
    dist2 = [987654321] * (N+1)                 # 가중치

    for _ in range(M):
        start, end, w = map(int, input().split())
        G1[start][end] = G2[end][start] = w

    dijkstra(X, G1, dist1)
    dijkstra(X, G2, dist2)

    ans = 0
    for i in range(1, N+1):
        if ans < dist1[i] + dist2[i]:
            ans = dist1[i] + dist2[i]

    print('#{} {}'.format(tc, ans))