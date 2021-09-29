import sys
sys.stdin = open('input.txt')
from collections import deque

t = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for idx in range(1, t+1):
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]
    dist = [[-1]*m for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'W':
                q.append((i, j))
                dist[i][j] = 0

    visited = [[0] * m for _ in range(n)]
    while q:
        a, b = q.popleft()
        for k in range(4):
            na = a + dx[k]
            nb = b + dy[k]
            if -1 < na < n and -1 < nb < m and dist[na][nb] == -1 and grid[na][nb] == 'L':
                dist[na][nb] = dist[a][b] + 1
                q.append((na, nb))
    print('#{} {}'.format(idx, sum(map(sum, dist))))