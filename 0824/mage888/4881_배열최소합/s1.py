import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]

    check = [[0] * N for _ in range(N)]
    print(check)
    mini = []

    min_value = 0
    for i in range(N):
        if min_value < nums[i][j]
        mini.append(min(nums[i]))
        check[i] == nums.index(min(nums[i]))


    # print('#{} {}'.format(tc, sum(cnt)))