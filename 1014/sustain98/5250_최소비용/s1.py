import sys
sys.stdin = open('input.txt')
import heapq


t = int(input())
INF = int(1e9)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for idx in range(1, t+1):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    dist = [[INF]*n for _ in range(n)]
    q = []
    heapq.heappush(q, (0, 0, 0))
    dist[0][0] = 0
    while q:
        w, x, y = heapq.heappop(q)
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < n and visited[nx][ny] == 0:
                if dist[nx][ny] > w + (g[nx][ny] - g[x][y] if g[nx][ny] - g[x][y] > 0 else 0) + 1:
                    dist[nx][ny] = w + (g[nx][ny] - g[x][y] if g[nx][ny] - g[x][y] > 0 else 0) + 1
                    heapq.heappush(q, (dist[nx][ny], nx, ny))

    print('#{} {}'.format(idx, dist[-1][-1]))


