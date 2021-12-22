import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dr = [1, 1, 1, 0, -1, -1, -1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

def dfs(r, c):
    v[r][c] = 1

    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < h and 0 <= nc < w:
            if arr[nr][nc] == 1:
                if not v[nr][nc]:
                    dfs(nr, nc)
    return

while True:
    w, h = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(h)]
    v = [[0] * w for _ in range(h)]

    if w == 0:
        break

    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and not v[i][j]:
                dfs(i, j)
                cnt += 1

    print(cnt)
