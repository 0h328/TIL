# 문제 푼 시간

import pathlib
import sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    e, n = map(int, input().split())
    tree = [[] for _ in range(e+2)]
    lst = list(map(int, input().split()))
    ans = 0

    for i in range(e):
        p, a = lst[i*2], lst[i*2+1]
        tree[p].append(a)

    def dfs(n: int):
        global ans
        ans += 1

        for node in tree[n]:
            dfs(node)

    dfs(n)
    print("#{} {}".format(test, ans))
