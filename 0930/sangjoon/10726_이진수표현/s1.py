# 문제 푼 시간
import pathlib
import sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    n, m = map(int, input().split())
    ans = "ON"
    for i in range(n):
        if not m & (1 << i):
            ans = "OFF"
            break

    print("#{} {}".format(test, ans))
