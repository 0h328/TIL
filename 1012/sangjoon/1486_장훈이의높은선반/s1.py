# 문제 푼 시간
import pathlib
import sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    n, b = map(int, input().split())
    lst = list(map(int, input().split()))
    res = 200000

    for i in range(1 << n):
        chk = 0
        for j in range(n):
            if i & (1 << j):
                chk += lst[j]

        if b <= chk < res:
            res = chk
    res -= b
    ans.append("#{} {}".format(test, res))

print(*ans, sep="\n")
