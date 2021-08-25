def dfs(r, c):
    global ans
    for i in range(4):                   # 네방향 탐색
        nr, nc = r + dr[i], c + dc[i]    # 위치 이동
        if 0 <= nr < N and 0 <= nc < N:  # 범위 체크
            if data[nr][nc] == 3:        # 만약 이동한 곳에서 도착지를 바로 만나면
                ans = 1                  # 그대로 종료
                return
            if not data[nr][nc] and not visited[nr][nc]:       # 이동한 위치가 통로(0) & 방문하지 않은 곳이라면
                visited[nr][nc] = 1                            # 방문처리 하고
                dfs(nr, nc)                                    # 해당 위치에서 재귀적으로 다시 탐색 시작

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    ans = 0
    for r in range(N):
        for c in range(N):
            if data[r][c] == 2:
                dfs(r, c)

    print('#{} {}'.format(tc, ans))