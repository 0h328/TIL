import sys
sys.stdin = open('input.txt')
from collections import deque


def bfs(x,y):
    visited = [[0] * n for _ in range(n)]
    q = deque([(x, y, 0)])
    visited[x][y] = 1
    while q:
        x, y, c = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if -1 < nx < n and -1 < ny < n and visited[nx][ny] == 0:
                if maze[nx][ny] == '3':
                    return c
                elif maze[nx][ny] == '0':
                    q.append((nx, ny, c+1))
                    visited[nx][ny] = 1
    return 0


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
t = int(input())
for idx in range(1, t+1):
    n = int(input())
    maze = []
    for i in range(n):
        sub = list(input())
        maze.append(sub)
        if '2' in sub:
            x, y = i, sub.index('2')

    print('#{} {}'.format(idx, bfs(x, y)))


