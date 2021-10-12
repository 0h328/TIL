import copy
import sys
sys.stdin = open('input.txt')


def check(num, r, c):
    k = num[r][c]
    visited[r][c] = 1
    for j in range(4):
        for l in range(1, k):
            nr = r + dr[j] * l
            nc = c + dc[j] * l
            if 0 <= nr < H and 0 <= nc < W and num[nr][nc] > 0 and not visited[nr][nc]:
                visited[nr][nc] = 1
                if num[nr][nc] > 1:
                    check(num, nr, nc)


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

    for h in range(H):
        if num[h][col]:
            check(num, h, col)
            for a in range(H):
                for b in range(W):
                    if visited[a][b]:
                        num[a][b] = 0
                        for c in range(a, 0, -1):
                            num[c][b], num[c-1][b] = num[c-1][b], num[c][b]
            visited = [[0] * W for _ in range(H)]
            break
    for i in range(W):
        work(num, cnt - 1, i)


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    visited = [[0]*W for _ in range(H)]
    result = 9*12*15
    sum_val = 0
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for z in range(W):
        work(arr, N, z)
    print('#{} {}'.format(tc, result))
