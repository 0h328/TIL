import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c):
    global v_cnt, o_cnt
    v[r][c] = 1

    if arr[r][c] == 'v':
        v_cnt += 1
    elif arr[r][c] == 'o':
        o_cnt += 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < R and 0 <= nc < C:
            if arr[nr][nc] != '#' and not v[nr][nc]:
                v[nr][nc] = 1
                dfs(nr, nc)


R, C = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
v = [[0] * C for _ in range(R)]

sheep = 0
wolf = 0

for i in range(R):
    for j in range(C):
        v_cnt = 0
        o_cnt = 0
        if arr[i][j] != '#' and not v[i][j]:
            dfs(i, j)

            if v_cnt >= o_cnt:
                o_cnt = 0
            else:
                v_cnt = 0

            sheep += o_cnt
            wolf += v_cnt

print(sheep, wolf)


