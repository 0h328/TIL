import sys
sys.stdin = open('input.txt')


def dfs(r, c, length, method):
    global result

    if length > 3 and (r, c) == first_idx:
        if length > result:
            result = length
            return
    for k in range(4):
        if k != method:
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and not visited[arr[nr][nc]]:
                visited[arr[nr][nc]] = 1
                dfs(nr, nc, length+1, (k+2)%4)
                visited[arr[nr][nc]] = 0
            if 0 <= nr < N and 0 <= nc < N and visited[arr[nr][nc]] == 2 and length != 1:
                dfs(nr, nc, length+1, (k+2)%4)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * 101
    result = -1
    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]
    condition = [(0, 0), (0, N-1), (N-1, 0), (N-1, N-1)]
    for i in range(N):
        for j in range(N):
            if (i, j) not in condition:
                visited[arr[i][j]] = 2
                first_idx = (i,j)
                dfs(i, j, 0, -1)
                visited[arr[i][j]] = 0


    print('#{} {}'.format(tc, result))