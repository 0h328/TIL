import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    max_num = 1
    min_num = 1e6

    for num in nums:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    print('#{} {}'.format(tc, max_num - min_num))