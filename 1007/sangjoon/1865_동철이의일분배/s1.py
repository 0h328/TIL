# 문제 푼 시간
import pathlib
import sys


sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def dfs(c, t):
    for i in range(n):
        if not visited[i]:
            nc = float(t*mp[c][i]/100)
            if nc > res[0]:
                if c + 1 == n:
                    res[0] = nc
                else:
                    visited[i] = 1
                    dfs(c+1, nc)
                    visited[i] = 0


ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    mp = [list(map(int, input().split())) for _ in range(n)]
    res = [0]
    visited = [0]*n
    dfs(0, float(1))
    ans.append("#{} {}".format(test, format(res[0]*100, ".6f")))

print(*ans, sep="\n")
