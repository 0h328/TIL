# 문제 푼 시간
import pathlib
import sys
from itertools import permutations

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    mp = [list(map(int, input().split())) for _ in range(n)]
    cnt = float("inf")

    for orders in permutations([i for i in range(1, n)], n-1):
        tmp = 0
        orders = [0] + list(orders) + [0]
        for i in range(n):
            tmp += mp[orders[i]][orders[i+1]]
        cnt = min(cnt, tmp)

    ans.append("#{} {}".format(test, cnt))

print(*ans, sep="\n")
