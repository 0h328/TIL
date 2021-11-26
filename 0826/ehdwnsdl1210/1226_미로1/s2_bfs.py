from pandas import DataFrame
# 0 길 / 1 벽 / 2 출발 / 3 도착
from collections import deque

dx = [0, 1, 0, -1]      # 우하좌상
dy = [1, 0, -1, 0]

def bfs(x, y):
    global result
    # q = []
    # q = q.deque()
    q = deque()     # deque([])
    q.append((x, y))

    while q:
        (x, y) = q.popleft()
        if maze[x][y] == 3:
            result = 1
            return

        maze[x][y] = 1
        for i in range(4):  # 우하좌상
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 16 and 0 <= ny < 16 and (nx, ny) not in q and (maze[nx][ny] == 0 or maze[nx][ny] == 3):
                q.append((nx, ny))

    return

import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())

    maze = [list(map(int, input())) for _ in range(16)]
    # print(maze)
    # print(DataFrame(maze))

    result = 0
    bfs(1, 1)
    print('#{} {}'.format(tc, result))