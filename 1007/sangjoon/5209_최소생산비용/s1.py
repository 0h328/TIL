# 문제 푼 시간
import pathlib
import sys


sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def dfs(cnt, cost):
    for i in range(n):
        if not visited[i]:
            nc = cost + mp[cnt][i]
            if nc < res[0]:
                if cnt + 1 == n:
                    res[0] = nc
                else:
                    visited[i] = 1
                    dfs(cnt+1, nc)
                    visited[i] = 0


ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    mp = [list(map(int, input().split())) for _ in range(n)]
    res = [float("inf")]
    visited = [0]*n
    dfs(0, 0)
    ans.append("#{} {}".format(test, res[0]))

print(*ans, sep="\n")
