def per(idx):
    global min_value, total

    if idx == N:
        pass

    for i in range(N):
        if check[i] == 0:
            total += nums[idx][i]
            check[i] = 1
            per(idx+1)
            check[i] = 0

    if min_value > total:
        min_value = total
        return

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N
    min_value = 91
    total = 0

    print('#{} {}'.format(tc, per(0)))
