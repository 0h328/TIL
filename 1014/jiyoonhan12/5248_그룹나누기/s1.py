import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(idx):
    global q, ans
    q.append(idx)
    visited[idx] = 1
    while q:
        i = q.popleft()
        for j in range(len(wish[i])):
            if not visited[wish[i][j]]:
                q.append(wish[i][j])
                visited[wish[i][j]] = 1
    ans += 1
    return

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    app = list(map(int, input().split()))
    wish = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    for i in range(len(app)//2):
        wish[app[i*2]].append(app[i*2+1])
        wish[app[i*2+1]].append(app[i*2])
    # print(wish)
    q = deque()
    ans = 0
    for k in range(1, N+1):
        if not visited[k]:
            bfs(k)
    print('#{} {}'.format(t, ans))