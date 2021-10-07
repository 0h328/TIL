import sys
sys.stdin = open('input.txt')


def dfs(r, c, cnt):
    global result
    if cnt > result:
        return
    if r == N-1:
        if cnt < result:
            result = cnt
    visited[c] = 1

    for k in range(N):
        nr = r + 1
        nc = k
        if 0 <= nr < N and 0 <= nc < N and not visited[nc]:
            dfs(nr, nc, cnt+arr[nr][nc])
    visited[c] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N + 1)
    result = 1500
    for i in range(N):
        dfs(0, i, arr[0][i])
    print('#{} {}'.format(tc, result))

