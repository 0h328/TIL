# 문제 푼 시간
import pathlib
import sys
from collections import defaultdict, deque

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    tr = defaultdict(set)
    res = [0]

    for i in range(m):
        v, c = lst[i*2], lst[i*2+1]
        tr[v].add(c)
        tr[c].add(v)

    visited = [0]*(n+1)
    for i in range(1, n+1):
        if not visited[i]:
            res[0] += 1
            dq = deque([i])
            while dq:
                e = dq.popleft()
                visited[e] = 1
                for c in tr[e]:
                    if not visited[c]:
                        dq.append(c)
    ans.append("#{} {}".format(test, res[0]))

print(*ans, sep="\n")
