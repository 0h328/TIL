import sys
sys.stdin = open('input.txt')


def dfs(r, c, d, w):
    global ans
    nr = r + dr[d]
    nc = c + dc[d]
    if (d + 1) % 4 == 0:
        if nr == temp_r and nc == temp_c and len(w) > ans:
            ans = len(w)
            return

    if 0 <= nr < N and 0 <= nc < N and D[nr][nc] not in w:
        dfs(nr, nc, d, w + [D[nr][nc]])
        dfs(nr, nc, (d + 1) % 4, w + [D[nr][nc]])


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    D = [list(input().split()) for _ in range(N)]
    dr = [-1, 1, 1, -1]
    dc = [1, 1, -1, -1]
    ans = -1

    for i in range(N):
        for j in range(N):
            temp_r = i
            temp_c = j
            dfs(i, j, 0, [D[i][j]])

    print('#{} {}'.format(test_case, ans))
