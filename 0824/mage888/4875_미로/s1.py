import sys
sys.stdin = open('input.txt')

def dfs(r, c):
    global ans

    rc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for dr, dc in rc:
        nr = r + dr
        nc = c + dc
        if nr in range(N) and nc in range(N) and not visited[nr][nc] and not maze[nr][nc]:
            visited[nr][nc] = 1
            dfs(nr, nc)
        elif nr in range(N) and nc in range(N) and maze[nr][nc] == 3:
            ans = 1
            return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    ans = 0

    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                dfs(r, c)

    print('#{} {}'.format(tc, ans))



