import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0

    for col in range(N - M + 1):
        nums_sum = 0
        for row in range(M):
            nums_sum += sum(nums[row][col:col+M])

        if nums_sum > max_sum:
            max_sum = nums_sum

        for row in range(N - M):
            nums_sum -= sum(nums[row][col:col+M])
            nums_sum += sum(nums[row+M][col:col+M])
            if nums_sum > max_sum:
                max_sum = nums_sum

    print('#{} {}'.format(t, max_sum))

