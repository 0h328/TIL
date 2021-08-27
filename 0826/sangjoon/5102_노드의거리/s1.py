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

        for n in grf[s]:
            if n == g:
                return cnt + 1
            if not visited[n]:
                visited[n] = 1
                dq.append([n, cnt + 1])

    return 0


test_case = int(input())

for test in range(1, test_case + 1):
    v, e = map(int, input().split())
    grf = {i: [] for i in range(v + 1)}

    for _ in range(e):
        n1, n2 = map(int, input().split())
        grf[n1].append(n2)
        grf[n2].append(n1)

    s, g = map(int, input().split())
    ans = bfs(s)

    print("#{} {}".format(test, ans))