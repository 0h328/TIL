import sys
sys.stdin = open('input.txt')

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
def dfs(r, c):
    for k in range(4):
        nr, nc = r+dr[k], c+dc[k]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1:
            if not visited[nr][nc]:
                visited[nr][nc] = 1
                dfs(nr, nc)

for T in range(int(input())):
    result = 0
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                sr, sc = r, c
            if arr[r][c] == 3:
                er, ec = r, c

    visited = [[0] * N for _ in range(N)]

    visited[sr][sc] = 1
    dfs(sr, sc)
    print('#{} {}'.format((T+1), visited[er][ec]))

#1 1
#2 1
#3 0
