# 문제 푼 시간
import pathlib
import sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    n, m = map(int, input().split())
    w = sorted(list(map(int, input().split())), reverse=True)
    t = sorted(list(map(int, input().split())), reverse=True)
    i = j = cnt = 0

    while i < len(w) and j < len(t):
        if t[j] >= w[i]:
            j += 1
            cnt += w[i]
        i += 1

    ans.append("#{} {}".format(test, cnt))

print(*ans, sep="\n")
