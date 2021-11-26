from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def bfs(node):
    q = deque()
    q.append(node)

    while q:
        p = q.popleft()
        for next_p in graph[p]:
            if not visited[next_p]:
                q.append(next_p)
                visited[next_p] = True


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    tmp = list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]

    for i in range(M):
        graph[tmp[i*2]].append(tmp[i*2 + 1])
        graph[tmp[i*2 + 1]].append(tmp[i*2])

    visited = [0] * (N + 1)
    answer = 0
    for n in range(1, N + 1):
        if not visited[n]:
            visited[n] = True
            answer += 1
            bfs(n)

    print('#{} {}'.format(tc, answer))
