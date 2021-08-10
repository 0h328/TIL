import sys

sys.stdin = open("input.txt")

test_case = int(input())
for test in range(1, test_case + 1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    max_sum, min_sum = 0, 10000 * m

    # 순차적으로 최대 최소값 탐색
    for i in range(n - m + 1):
        sum_nums = sum(nums[i : i + m])
        if sum_nums < min_sum:
            min_sum = sum_nums
        if sum_nums > max_sum:
            max_sum = sum_nums

    ans = max_sum - min_sum

    print("#{} {}".format(test, ans))