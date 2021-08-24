# 문제 푼 시간
# 풀이법: bfs 사용
from collections import deque


def bfs(x: int, y: int):
    dq = deque([[x, y]])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    mp[x][y] = "1"

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if mp[nx][ny] == "3":
                    return 1

                elif mp[nx][ny] == "0":
                    mp[nx][ny] = "1"
                    dq.append([nx, ny])
    return 0


import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    mp = [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if mp[i][j] == "2":
                ans = bfs(i, j)

    print("#{} {}".format(test, ans))
