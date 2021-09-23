def dfs(r, c):
    global ans
    if data[r][c] == 3:         # 도착하면
        ans = 1                 # 값 바꾸고
        return                  # 종료
    visited[r][c] = 1           # 방문체크

    for i in range(4):          # 4방 탐색
        nr = r + dr[i]
        nc = c + dc[i]
        if (0 <= nr < N) and (0 <= nc < N):                 # 범위 체크
            if not visited[nr][nc] and data[nr][nc] != 1:   # 방문 안했고 벽이 아니면
                dfs(nr, nc)                                 # 재귀 호출

import sys
sys.stdin = open('input.txt')
for _ in range(10):
    tc = int(input())
    N = 16
    data = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    ans = 0
    for r in range(N):
        for c in range(N):
            if data[r][c] == 2:
                dfs(r, c)
    print('#{} {}'.format(tc, ans))