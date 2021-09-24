# 문제 푼 시간

import pathlib
import sys
from collections import deque

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test = int(input())

for test_case in range(1, test+1):
    n, m = map(int, input().split())
    gh = [list(input()) for _ in range(n)]
    visited = [[-1] * m for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    dq = deque([])

    ans = 0

    # 시작지점 표시
    for i in range(n):
        for j in range(m):
            if gh[i][j] == "W":
                visited[i][j] = 0
                dq.append((i, j))

    # bfs 탐색
    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                ans += visited[x][y] + 1
                dq.append((nx, ny))

    print(f"#{test_case} {ans}")
