import sys
sys.stdin = open('input.txt')

def dfs(r, c):
    global result
    if arr[r][c] == 3:
        result = 1
        return
    for k in range(4):
        nr, nc = r + dy[k], c + dx[k]
        if 0 <= nr < N and 0 <= nc <N:
            if arr[nr][nc] != 1 and visited[nr][nc] != 1:
                visited[nr][nc] = 1
                dfs(nr, nc)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                row = i
                col = j
    dfs(row,col)
    print('#{} {}'.format(tc, result))



