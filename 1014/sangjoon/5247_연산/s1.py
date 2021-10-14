# 문제 푼 시간
import pathlib
import sys
from collections import deque
sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def bfs(n):
    dq = deque([n])
    ev = [lambda x: x+1, lambda x: x-1, lambda x: x*2, lambda x: x-10]

    while dq:
        e = dq.popleft()
        for d in ev:
            ne = d(e)
            if 0 <= ne < max(n, m)*2 and not dp[ne]:
                if ne == m:
                    return dp[e] + 1
                dp[ne] = dp[e] + 1
                dq.append((ne))


ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    n, m = map(int, input().split())
    dp = [0]*(max(n, m)*2)
    res = bfs(n)
    ans.append("#{} {}".format(test, res))

print(*ans, sep="\n")
