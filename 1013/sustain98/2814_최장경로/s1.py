import sys
sys.stdin = open('input.txt')
from collections import deque

t = int(input())
for idx in range(1, t+1):
    n, m = map(int, input().split())
    l = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        l[x].append(y)
        l[y].append(x)

    q = deque([(i, 1 << i, 1) for i in range(1, n+1)])
    while q:
        node, visited, cnt = q.popleft()
        for i in l[node]:
            if not visited & (1 << i):
                q.append((i, visited | (1 << i), cnt + 1))
    print('#{} {}'.format(idx, cnt))

