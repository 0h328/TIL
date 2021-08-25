# 문제 푼 시간
# 풀이법: dfs
def dfs(x: int, y: int):
    global ans
    if mp[x][y] == "3":  # 종료 조건
        ans = 1  # 최종지점 방문 표시
        return

    mp[x][y] = "1"

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if mp[nx][ny] != "1":  # 이동가능할 경우
                dfs(nx, ny)


import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    mp = [list(input()) for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    ans = 0

    for i in range(n):
        for j in range(n):
            if mp[i][j] == "2":
                dfs(i, j)

    print("#{} {}".format(test, ans))
