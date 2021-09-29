import sys
sys.stdin = open('input.txt')

# x: 우, y: 좌, h: 높이, go: 갈수있는 길 do: 공사진행
def dfs(x, y, h, go, do):
    global cnt
    visited[r][c] = 1

    if cnt < go:
        cnt = go

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr in range(N) and nc in range(N):
            if h > data[nr][nc]:
                dfs(nr, nc, data[nr][nc], go+1, do)
            elif h > data[nr][nc]-K:
                dfs(nr, nc, data[r][c]-K, go+1, 0)

    visited[r][c] = 0


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    max_height = 0
    for r in range(N):
        for c in range(N):
            if max_height < data[r][c]:
                max_height = data[r][c]

    for r in range(N):
        for c in range(N):
            if data[r][c] == max_height:
                dfs(r, c, max_height, 1, 1)

    print('#{} {}'.format(tc, cnt))




