# 문제 푼 시간
# 풀이법: dfs 재귀

import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

# dfs 완전탐색
def dfs(n: str):
    visited[n] = 1

    for node in graph[n]:
        if not visited[node]:
            dfs(node)


test_case = 10

for test in range(1, test_case + 1):
    test, n = map(int, input().split())
    lst = list(map(int, input().split()))
    graph = [[] for _ in range(100)]  # 그래프 초기화
    visited = [0] * (100)  # 방문초기화

    for i in range(0, 2 * n, 2):  # 그래프 생성
        graph[lst[i]].append(lst[i + 1])

    dfs(0)  # dfs 탐색
    ans = 1 if visited[-1] else 0  # 마지막 도착시 1 출력

    print("#{} {}".format(test, ans))