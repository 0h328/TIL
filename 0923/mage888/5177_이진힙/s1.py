import heapq
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    nums = []
    for v in data:
        heapq.heappush(nums, v)

    nums = [0] + nums
    ans = 0

    while N > 1:
        ans += nums[N//2]
        N //= 2

    print('#{} {}'.format(tc, ans))