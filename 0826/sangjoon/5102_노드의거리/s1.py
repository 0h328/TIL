# 문제 푼 시간
# 풀이법: BFS 사용
import pathlib, sys
from collections import deque

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def bfs(s: int):
    visited = [0] * (v + 1)
    dq = deque([[s, 0]])

    while dq:
        s, cnt = dq.popleft()

        if s in gh:
            for n in gh[s]:
                if n == g:
                    return cnt + 1
                if not visited[n]:
                    visited[n] = 1
                    dq.append([n, cnt + 1])

    return 0


test_case = int(input())

for test in range(1, test_case + 1):
    v, e = map(int, input().split())
    gh = {}
    for _ in range(e):
        n1, n2 = map(int, input().split())
        if gh.get(n1):
            gh[n1].append(n2)
        else:
            gh[n1] = [n2]
        if gh.get(n2):
            gh[n2].append(n1)
        else:
            gh[n2] = [n1]

    s, g = map(int, input().split())
    ans = bfs(s)

    print("#{} {}".format(test, ans))