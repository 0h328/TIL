import copy
import sys
sys.stdin = open('input.txt')


def check(num, r, c, k):
    for j in range(4):
        for l in range(1, k):
            nr = r + dr[j] * l
            nc = c + dc[j] * l
            if 0 <= nr < H and 0 <= nc < W and num[nr][nc] > 0:
                tmp = num[nr][nc]
                num[nr][nc] = 0
                if tmp > 1:
                    check(num, nr, nc, tmp)


def work(nums, cnt, col):
    global result, visited, sum_val
    num = copy.deepcopy(nums)
    if cnt == 0:
        for a in range(H):
            for b in range(W):
                if num[a][b]:
                    sum_val += 1
        if sum_val < result:
            result = sum_val
        sum_val = 0
        return
    buck_down = num
    for h in range(H):
        if num[h][col]:
            itmp = num[h][col]
            num[h][col] = 0
            check(num, h, col, itmp)
            buck_down = [[0 for _ in range(W)] for _ in range(H)]
            for d in range(W):
                temp = []
                for e in range(H):
                    if num[e][d]:
                        temp.append(num[e][d])
                for j in range(len(temp)):
                    buck_down[H - len(temp) + j][d] = temp[j]
            break
    for i in range(W):
        work(buck_down, cnt - 1, i)


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]

    result = 9*12*15
    sum_val = 0
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for z in range(W):
        work(arr, N, z)
    print('#{} {}'.format(tc, result))
