import sys
sys.stdin = open('input.txt')


def dfs(r, c, length):
    global result
    if (r, c) == (N-1, N-1):
        if length < result:
            result = length
        return
    if length >= result:
        return
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if arr[nr][nc] > arr[r][c]:
                visited[nr][nc] = 1
                dfs(nr, nc, length + arr[nr][nc] - arr[r][c] + 1)
                visited[nr][nc] = 0
            else:
                visited[nr][nc] = 1
                dfs(nr, nc, length + 1)
                visited[nr][nc] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    result = 10000000000000000000000
    visited = [[0]*N for _ in range(N)]
    visited[0][0] = 1
    dfs(0, 0, 0)
    print('#{} {}'.format(tc, result))