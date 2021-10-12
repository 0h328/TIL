import sys

sys.stdin = open('input.txt')
# 아래로 내리기

def dfs_back(N):
    while stack[N]:
        nr, nc, num = stack[N].pop()
        arr[nr][nc] = num


def dfs(r, c, num, N):
    global curr_breaks
    stack[N].append((r, c, num))

    for d in range(4):
        for j in range(1, num + 1):
            nr, nc = r + (dr[d] * j), c + (dc[d] * j)
            if 0 <= nr < H and 0 <= nc < W:
                n_num = arr[nr][nc]
                if n_num > 1:
                    arr[nr][nc] = 0
                    curr_breaks += 1
                    dfs(nr, nc, n_num, N)


def choose_brick(cnt_N):
    global max_breaks, curr_breaks

    if cnt_N == N:
        if curr_breaks > max_breaks:
            max_breaks = curr_breaks
        return

    for j in range(W):
        curr_breaks = 0
        for i in range(H):
            if arr[i][j] == 1:
                stack[N].append((i, j))
                arr[i][j] = 0
                curr_breaks += 1
                break
            elif arr[i][j] > 1:
                dfs(i, j, arr[i][j], cnt_N)
                break

        # print(i, j)
        # for h in range(H):
        #     print(arr[h])
        choose_brick(cnt_N + 1)
        dfs_back(cnt_N)

T = int(input())

for t in range(1, T + 1):
    N, W, H = map(int, input().split())  # N: 벽돌깨는 횟수, W: 가로, H: 세로
    arr = [list(map(int, input().split())) for _ in range(H)]
    max_breaks = 0
    curr_breaks = 0
    dr = [0, 1, 0, -1] #우하좌상
    dc = [1, 0, -1, 0]
    stack = [[] for _ in range(N)]

    choose_brick(0)

    print('#{} {}'.format(t, max_breaks))