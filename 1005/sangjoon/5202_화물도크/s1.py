# 문제 푼 시간
import pathlib
import sys


sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


test_case = int(input())
ans = []
for test in range(1, test_case + 1):
    n = int(input())
    lst = [tuple(map(int, input().split())) for _ in range(n)]
    lst.sort(key=lambda x: (x[1], x[0]))
    cnt = 1
    s, e = lst[0]
    for ts, te in lst:
        if ts >= e:
            cnt += 1
            e = te

    ans.append("#{} {}".format(test, cnt))

print(*ans, sep="\n")
