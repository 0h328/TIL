import sys
sys.stdin = open('input.txt')

# 0: 통로, 1: 벽, 2: 출발, 3: 도착

def dfs(r, c):
    global ans
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            if maze[nr][nc] == 3:
                ans = 1
                return
            if not maze[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = 1
                dfs(nr, nc)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    r, c = 0, 0
    ans = 0

    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                dfs(r, c)

    print('#{} {}'.format(tc, ans))



