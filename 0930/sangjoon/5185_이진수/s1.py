# 문제 푼 시간
import pathlib
import sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    n, s = map(list, input().split())
    ans = ""
    for i in s:
        ans += format(int(i, 16), "b").zfill(4)
    print("#{} {}".format(test, ans))
