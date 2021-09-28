# 문제 푼 시간

import pathlib
import sys
from collections import deque

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def bfs(x, y):
    global ans
    dq = deque([(x, y, 1)])
    visited[x][y] = 1

    while dq:
        ans += 1
        x, y, cnt = dq.popleft()
        for i in turnel[gh[x][y]]:
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:  # 이동가능 확인
                if gh[nx][ny]:  # 터널확인
                    for s in turnel[gh[nx][ny]]:
                        if abs(i-s) == 2 and cnt < l:
                            visited[nx][ny] = 1
                            dq.append((nx, ny, cnt + 1))


test = int(input())

for test_case in range(1, test+1):
    n, m, r, c, l = map(int, input().split())
    gh = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    # 상:0 좌:1 하:2 우:3
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    turnel = {
        1: [0, 1, 2, 3],
        2: [0, 2],
        3: [1, 3],
        4: [0, 3],
        5: [2, 3],
        6: [1, 2],
        7: [0, 1],
    }

    ans = 0

    bfs(r, c)
    print(f"#{test_case} {ans}")
