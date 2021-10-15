import sys
sys.stdin = open('input.txt')
from collections import deque


def dijstra(start, adj, dist):
    dist[start] = 0
    q = deque([start])
    while q:
        i = q.popleft()
        for j in range(N+1):
            if adj[i][j]:
                temp = dist[i] + adj[i][j]
                if temp < dist[j]:
                    dist[j] = temp
                    q.append(j)
    return dist


T = int(input())
for t in range(1, T+1):
    N, M, X = map(int, input().split())
    adj1 = [[987654321] * (N+1) for _ in range(N+1)] # 원래 입력(진출)
    adj2 = [[987654321] * (N+1) for _ in range(N+1)] # 뒤집은 입력 (진입)

    for _ in range(M):
        x, y, c = map(int, input().split())
        adj1[x][y] = c
        adj2[y][x] = c

    dist1 = [987654321] * (N+1)
    dist2 = [987654321] * (N+1)

    max_value = 0
    dijstra(X, adj1, dist1)
    dijstra(X, adj2, dist2)

    for i in range(1, N+1):
        if dist1[i] + dist2[i] > max_value:
            max_value = dist1[i] + dist2[i]

    print('#{} {}'.format(t, max_value))