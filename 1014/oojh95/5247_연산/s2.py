import sys
from collections import deque
sys.stdin = open('input.txt')


def bfs(n, cnt):
    global result
    Q = deque()
    Q.append((n, cnt))
    while Q:
        a, b = Q.popleft()
        if a == M:
            result = b
            return
        if visited.get(a, 0):
            continue
        visited[a] = 1
        if a * 2 <= 1000000:
            Q.append((a*2, b+1))
        if a + 1 <= 1000000:
            Q.append((a+1, b+1))
        if 0 < a - 1 <= 1000000:
            Q.append((a - 1, b + 1))
        if 0 < a - 10 <= 1000000:
            Q.append((a-10, b+1))

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = 1000000
    visited = {}
    bfs(N, 0)
    print('#{} {}'.format(tc, result))