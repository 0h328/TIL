import sys
sys.stdin = open('input.txt')

def dfs(r, c, cnt):
    global min_result
    visited[r][c] = 1
    cnt += arr[r][c]
    if cnt < min_result:
        if r == c == N-1:
            if cnt < min_result:
                min_result = cnt

        for i in range(2):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                dfs(nr, nc, cnt)
        visited[r][c] = 0
    else:
        visited[r][c] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_result = 10*N*N
    visited = [[0]*N for _ in range(N)]
    dr = [1, 0]
    dc = [0, 1]
    dfs(0, 0, 0)
    print('#{} {}'.format(tc, min_result))
