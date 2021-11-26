import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')


def bfs(s, g):
    visited = [0] * (v+1)
    q = deque([(s, 0)])
    visited[s] = 1
    while q:
        x, cnt = q.popleft()
        for node in edges[x]:
            if visited[node] == 0:
                if node == g:
                    return cnt+1
                visited[node] = 1
                q.append((node, cnt+1))
    return 0


t = int(input())
for idx in range(1, t+1):
    edges = defaultdict(list)
    v, e = map(int, input().split())
    for _ in range(e):
        s, g = map(int, input().split())
        edges[s].append(g)
        edges[g].append(s)
    s, g = map(int, input().split())

    print('#{} {}'.format(idx, bfs(s, g)))