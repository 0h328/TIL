# 문제 푼 시간
import pathlib
import sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    n = float(input())
    i = 1
    ans = ""
    while n:
        if i > 12:
            ans = "overflow"
            break
        if n >= 2 ** (-i):
            n -= 2 ** (-i)
            ans += "1"
        else:
            ans += "0"
        i += 1

    print("#{} {}".format(test, ans))
