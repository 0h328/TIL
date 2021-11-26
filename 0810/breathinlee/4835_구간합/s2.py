import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    max_val = 0
    min_val = 1e6

    for i in range(N-M+1):
        my_sum = sum(nums[i:i+M])
        if max_val < my_sum:
            max_val = my_sum
        if min_val > my_sum:
            min_val = my_sum

    print('#{} {}'.format(tc, max_val - min_val))