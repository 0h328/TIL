from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def bfs(start):
    visited = [0] * 1000001
    visited[start] = 1
    q = deque()
    q.append(start)

    while q:
        p = q.popleft()

        if p == M:
            return visited[p] - 1

        for next_p in [p + 1, p - 1, p * 2, p - 10]:
            if 0 < next_p <= 1000000 and not visited[next_p]:
                q.append(next_p)
                visited[next_p] = visited[p] + 1


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    answer = bfs(N)
    print('#{} {}'.format(tc, answer))