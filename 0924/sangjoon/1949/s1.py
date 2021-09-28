# 문제 푼 시간

import pathlib
import sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def dfs(x, y, cnt, check):
    global ans
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 방문가능 확인
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:

            if graph[nx][ny] < graph[x][y]:
                dfs(nx, ny, cnt+1, check)
                continue

            # 지형을 깍지 않았을 경우
            if not check:
                for k in range(1, K+1):
                    if graph[nx][ny]-k < graph[x][y]:
                        graph[nx][ny] -= k
                        dfs(nx, ny, cnt+1, True)
                        graph[nx][ny] += k
                        break

    ans = max(ans, cnt)
    visited[x][y] = 0


test = int(input())

for test_case in range(1, test+1):
    N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    mh = 0

    # 최대 위치
    for i in range(N):
        for j in range(N):
            if graph[i][j] > mh:
                mh, mh_lst = graph[i][j], []
            if graph[i][j] == mh:
                mh_lst.append((i, j))

    # 최대 높이 기준 dfs 탐색
    for x, y in mh_lst:
        visited = [[0]*N for _ in range(N)]
        dfs(x, y, 1, False)

    print(f"#{test_case} {ans}")
