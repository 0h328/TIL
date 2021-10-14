import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c, f):
    global ans
    if f >= ans:
        return

    if r == N-1 and c == N-1:
        if ans > f:
            ans = f
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if not visited[nr][nc]:
                visited[nr][nc] = 1
                if H[r][c] >= H[nr][nc]:
                    dfs(nr, nc, f + 1)
                    visited[nr][nc] = 0
                else:
                    dfs(nr, nc, f + 1 + H[nr][nc] - H[r][c])
                    visited[nr][nc] = 0


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]
    ans = 987654321
    visited = [[0] * N for _ in range(N)]
    dfs(0, 0, 0)
    print('#{} {}'.format(test_case, ans))