from pandas import DataFrame
from collections import deque
# 0 통로 / 1 벽 / 2 출발 / 3 도착

dx = [0, 1, 0, -1]      # 우하좌상
dy = [1, 0, -1, 0]

def bfs(x, y, n):
    q = deque()
    q.append((x, y, n))

    while q:
        (x, y, n) = q.popleft()
        if maze[x][y] == 3:
            return n - 2

        maze[x][y] = 1          # ㅄ / 이게 visited 같은거네 (1로 만들어서 다시 안보게)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in q and (maze[nx][ny] == 0 or maze[nx][ny] == 3):
                q.append((nx, ny, n+1))

    return 0

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    maze = [list(map(int, input())) for _ in range(N)]
    # print(maze)
    # print(DataFrame(maze))

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x, y = i, j

    print('#{} {}'.format(tc, bfs(x, y, 1)))