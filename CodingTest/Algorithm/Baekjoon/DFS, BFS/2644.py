import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(t1, t2):
    q = deque()
    q.append((t1, 0))
    v[t1] = 1

    while q:
        now, cnt = q.popleft()

        if now == t2:
            print(cnt)
            return

        for i in G[now]:
            if not v[i]:
                q.append((i, cnt+1))
                v[i] = 1

    print(-1)


n = int(input())
p1, p2 = map(int, sys.stdin.readline().split())

G = [[] for _ in range(n+1)]
v = [0] * (n+1)

m = int(input())
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    G[x].append(y)
    G[y].append(x)

bfs(p1, p2)

