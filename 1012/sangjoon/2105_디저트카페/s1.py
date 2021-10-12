# 문제 푼 시간
def dfs(x, y, d):
    global ans

    for k in range(2):
        d += k if d < 3 else 0
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < N:  # 이동 가능할 경우
            if d == 3 and (nx, ny) == start:  # 종료조건
                cnt = len(dessert) if len(dessert) > 2 else -1
                ans = max(ans, cnt)
                return

            if mp[nx][ny] not in dessert:
                dessert.append(mp[nx][ny])
                dfs(nx, ny, d)
                dessert.pop()


test = int(input())

for test_case in range(1, test+1):
    N = int(input())
    mp = [list(map(int, input().split())) for _ in range(N)]
    # 시계방향 회전
    dx = [1, 1, -1, -1]
    dy = [1, -1, -1, 1]
    ans = -1

    for i in range(N-2):
        for j in range(1, N-1):
            if mp[i][j] != mp[i+1][j+1]:
                start = (i, j)
                dessert = [mp[i][j], mp[i+1][j+1]]
                dfs(i+1, j+1, 0)

    print(f"#{test_case} {ans}")
