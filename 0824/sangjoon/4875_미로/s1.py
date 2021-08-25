# 문제 푼 시간
# 풀이법: bfs 사용
from collections import deque


def bfs(x: int, y: int):
    dq = deque([[x, y]])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    mp[x][y] = "1"  # 방문표시 초기화 : -> while문 안에 보통 사용하나요?

    while dq:
        x, y = dq.popleft()
        print(mp)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if mp[nx][ny] == "3":  # deque에 넣기전에 종료
                    return 1

                elif mp[nx][ny] == "0":  # 이동가능 할경우
                    mp[nx][ny] = "1"  # 방문표시
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
                ans = bfs(i, j)  # 시작위치 탐색

    print("#{} {}".format(test, ans))
