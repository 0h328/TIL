import sys
sys.stdin = open('input.txt')
from collections import deque


def calc(now, i):
    if i == 0:
        return now + 1
    elif i == 1:
        return now - 1
    elif i == 2:
        return now * 2
    else:
        return now - 10

def bfs(n, m):
    global visited
    q = deque()
    q.append((n, 0))
    visited[n] = 1
    while q:
        now, cnt = q.popleft()
        for i in range(4):
            next = calc(now, i)
            if next == m:
                return cnt + 1
            elif 1 <= next <= 1000000 and not visited[next]:
                q.append((next, cnt+1))
                visited[next] = 1

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    print('#{} {}'.format(t, bfs(N, M)))