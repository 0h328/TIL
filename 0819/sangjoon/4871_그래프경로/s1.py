# 문제 푼 시간 5분 / 10분
# 풀이법: dfs로 구현


def dfs(s: int):
    visited[s] = 1
    for node in graph[s]:
        if not visited[node]:
            dfs(node)


import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)

    s, g = map(int, input().split())
    dfs(s)
    ans = visited[g]
    print("#{} {}".format(test, ans))