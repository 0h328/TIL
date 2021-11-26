# 문제 푼 시간
import pathlib
import sys


def dfs(v: int, cnt: int, visited: set):

    for c in tr[v]:
        if c not in visited:
            visited = visited | set([c])
            dfs(c, cnt+1, visted)
            visited -= set([c])

    res[0] = max(res[0], cnt)


sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    n, m = map(int, input().split())
    tr = [[] for _ in range(n+1)]
    res = [0]

    for _ in range(m):
        v, c = map(int, input().split())
        tr[v].append(c)
        tr[c].append(v)

    for i in range(n+1):
        dfs(i, 1, set([i]))

    ans.append("#{} {}".format(test, res[0]))

print(*ans, sep="\n")
