import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    res_max = 0
    res_min = 1000000
    for i in range(N-M+1):
        cnt = 0
        for j in range(i, i+M):
            cnt += nums[j]
        if res_max < cnt:
            res_max = cnt
        if res_min > cnt:
            res_min = cnt
    res = res_max - res_min

    print('#{} {}'.format(tc, res))
