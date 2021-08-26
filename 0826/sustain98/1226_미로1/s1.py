import sys
from collections import deque
sys.stdin = open('input.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for idx in range(1, 11):
    idx = input()
    res = 0
    maze = []
    visited = [[0]*16 for _ in range(16)]
    for i in range(16):
        sub = list(input())
        maze.append(sub)
        if '2' in sub:
            x, y = i, sub.index('2')

    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if -1 < nx < 16 and -1 < ny < 16 and visited[nx][ny] == 0:
                if maze[nx][ny] == '3':
                    res = 1
                    q.clear()
                    break
                elif maze[nx][ny] == '0':
                    q.append((nx, ny))
                    visited[nx][ny] = 1

    print('#{} {}'.format(idx, res))


