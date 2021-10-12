import sys

sys.stdin = open('input.txt')


# 아래로 내리기


def make_arr(bricks):
    arr = [[] for _ in range(W)]
    for i in range(W):
        for j in range(H):
            arr[j].append(bricks[i][j])
    return arr


def dfs(r, c, num, N):
    global curr_breaks

    for d in range(4):
        for j in range(1, num + 1):
            nr, nc = r + (dr[d] * j), c + (dc[d] * j)
            if 0 <= nr < H and 0 <= nc < W:
                n_num = arr[nr][nc]
                if n_num > 1:
                    arr[nr][nc] = -1
                    curr_breaks += 1
                    dfs(nr, nc, n_num, N)
                elif n_num == 1:
                    arr[nr][nc] = -1
                    curr_breaks += 1


def choose_brick(cnt_N):
    global max_breaks, curr_breaks, arr

    if cnt_N == N:
        if curr_breaks > max_breaks:
            max_breaks = curr_breaks
        return

    for i in range(W):
        curr_breaks = 0
        for j in range(H):
            if arr[i][j] == 1:
                arr[i][j] = -1
                curr_breaks += 1
                choose_brick(cnt_N + 1)
                break
            elif arr[i][j] > 1:
                temp_arr = make_arr(arr)
                dfs(i, j, arr[i][j], cnt_N)
                choose_brick(cnt_N + 1)
                arr = temp_arr
                break

        # print(i, j)
        # for h in range(H):
        #     print(arr[h])


T = int(input())

for t in range(1, T + 1):
    N, W, H = map(int, input().split())  # N: 벽돌깨는 횟수, W: 가로, H: 세로
    bricks = [list(map(int, input().split())) for _ in range(H)]


    max_breaks = 0
    curr_breaks = 0
    dr = [0, 1, 0, -1]  # 우하좌상
    dc = [1, 0, -1, 0]
    stack = [[] for _ in range(N)]

    arr = [[] for _ in range(W)]
    for i in range(H):
        for j in range(W):
            arr[j].append(bricks[i][j])
    print(arr)
    choose_brick(0)

    print('#{} {}'.format(t, max_breaks))
