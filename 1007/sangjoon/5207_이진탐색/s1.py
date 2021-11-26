# 문제 푼 시간
import pathlib
import sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))
    res = 0
    ans.append("#{} {}".format(test, res))

print(*ans, sep="\n")
