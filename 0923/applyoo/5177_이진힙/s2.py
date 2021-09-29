from heapq import heappush
import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    res = []
    for v in arr:
        heappush(res, v)

    res.insert(0, 0)
    idx = N
    ans = -res[idx]

    while idx:
        ans += res[idx]
        idx //= 2

    print('#{0} {1}'.format(tc, ans))
