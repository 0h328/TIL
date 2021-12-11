import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, armor):
    global cnt

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == armor and not visited[nr][nc]:
            visited[nr][nc] = 1
            cnt += 1
            dfs(nr, nc, armor)
    
    return

N, M = map(int, input().split())
arr = [list(input()) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
white, black = 0, 0

for i in range(M):
    for j in range(N):
        cnt = 1
        if not visited[i][j]:
            if arr[i][j] == 'W':
                visited[i][j] = 1
                dfs(i, j, 'W')
                white += cnt**2
            else:
                visited[i][j] = 1
                dfs(i, j, 'B')
                black += cnt**2

print(white, black)