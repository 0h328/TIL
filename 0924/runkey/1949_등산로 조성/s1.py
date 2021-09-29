import sys
sys.stdin = open('input.txt')

tc = int(input())

def walking(r, c, skill, move):
    global cnt

    if move > cnt:
        cnt = move

    visited[r][c] = 1

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if map_list[nr][nc] < map_list[r][c]:
                walking(nr, nc, skill, move + 1)
            elif skill and map_list[nr][nc] - K < map_list[r][c]:
                temp = map_list[nr][nc]
                map_list[nr][nc] = map_list[r][c] - 1
                walking(nr, nc, 0, move + 1)
                map_list[nr][nc] = temp

    visited[r][c] = 0

for t in range(1, tc + 1):
    result = 0
    cnt = 0
    N, K = map(int, input().split())
    map_list = [list(map(int, input().split())) for _ in range(N)]

    max_num = 0
    for i in range(N):
        for j in range(N):
            if max_num < map_list[i][j]:
                max_num = map_list[i][j]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if map_list[i][j] == max_num:
                walking(i, j, 1, 1)

    result = cnt

    print("#{} {}".format(t, result))