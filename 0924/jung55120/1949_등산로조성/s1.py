import sys
sys.stdin = open('input.txt')

# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def find_road(r, c, length, check):
    global result
    if length > result:
        result = length

    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if land[r][c] > land[nr][nc]:
                find_road(nr, nc, length + 1, check)
            elif check and land[r][c] > land[nr][nc] - K:
                temp = land[nr][nc]
                land[nr][nc] = land[r][c] - 1
                find_road(nr, nc, length + 1, 0)
                land[nr][nc] = temp

    visited[r][c] = 0


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(N)]
    # print(land)
    max_num = 0
    for i in range(N):
        for j in range(N):
            if max_num < land[i][j]:
                max_num = land[i][j]

    visited = [[0] * N for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            if max_num == land[i][j]:
                find_road(i, j, 1, 1)

    print('#{} {}'.format(tc, result))
