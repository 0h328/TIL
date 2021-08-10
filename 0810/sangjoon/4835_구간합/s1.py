import sys

sys.stdin = open("input.txt")

test_case = int(input())
for test in range(1, test_case + 1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    max_sum, min_sum = 0, 10000 * m

    # 구간합 사용
    prefix = [0]
    ans = 0

    sum_value = 0
    for num in nums:
        sum_value += num
        prefix.append(sum_value)

    # 구간별 최대 최소 탐색
    for i in range(n - m + 1):
        sum_nums = prefix[i + m] - prefix[i]
        if sum_nums < min_sum:
            min_sum = sum_nums
        if sum_nums > max_sum:
            max_sum = sum_nums

    ans = max_sum - min_sum

    print("#{} {}".format(test, ans))
