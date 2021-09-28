# 문제 푼 시간

import pathlib
import sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def dfs(n, cost):
    global ans
    if n > 11:
        ans = min(ans, cost)
        return

    if schedule[n]:
        dfs(n+1, cost + min(schedule[n]*d, m1))
        dfs(n+3, cost + m3)

    else:
        dfs(n+1, cost)


test = int(input())

for test_case in range(1, test+1):
    d, m1, m3, y = map(int, input().split())
    schedule = list(map(int, input().split()))
    ans = y

    dfs(0, 0)
    print(f"#{test_case} {ans}")
