# 문제 푼 시간
import pathlib
import sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    v, e = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(e)]
    edges.sort(key=lambda x: x[2])
    parent = [0]*(v+1)
    res = [0]

    for i in range(1, v+1):
        parent[i] = i

    for n1, n2, w in edges:
        if find(n1) != find(n2):
            union(n1, n2)
            res[0] += w

    ans.append("#{} {}".format(test, res[0]))

print(*ans, sep="\n")
