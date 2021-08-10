import sys

sys.stdin = open("input.txt")

test_case = int(input())
for test in range(1, test_case + 1):
    n, nums = int(input()), list(map(int, input().split()))
    max_num, min_num = 1, 1000000

    for num in nums:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    ans = max_num - min_num
    print("#{} {}".format(test, ans))
