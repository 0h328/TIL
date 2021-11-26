import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c, cnt):
    global tmp
    v[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 1 <= nr < N+1 and 1 <= nc < M+1 and not v[nr][nc] and trash[nr][nc]:
            v[nr][nc] = 1
            cnt = dfs(nr, nc, cnt+1)
    return cnt

N, M, K = map(int,input().split())
trash = [[0] * (M+1) for _ in range(N+1)]
v = [[0] * (M+1) for _ in range(N+1)]

for _ in range(K):
    r, c = map(int, input().split())
    trash[r][c] = 1

tmp = []
for i in range(1, N+1):
    for j in range(1, M+1):
        if trash[i][j] == 1:
            tmp.append(dfs(i, j, 1))

print(max(tmp))


