# 문제 푼 시간
# 풀이법: Count 사용
from collections import deque
import pathlib, sys


sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def bfs(x: int, y: int):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dq = deque([[x, y, 0]])  # 디큐 초기화

    while dq:
        x, y, cnt = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if mp[nx][ny] == 3:  # 도착지에 도착했을 경우
                    return cnt

                if mp[nx][ny] == 0:
                    mp[nx][ny] = 1  # 방문 표시
                    dq.append([nx, ny, cnt + 1])  # 이동 가능할 겨우

    return 0  # 목적지에 도착하지 못할 경우


test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    mp = [list(map(int, input())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if mp[i][j] == 2:
                ans = bfs(i, j)

    print("#{} {}".format(test, ans))