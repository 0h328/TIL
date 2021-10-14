import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())
    road = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        road[s].append((e, w))
    dist = [1E7] * (N+1)
    q = deque([0])
    dist[0] = 0
    while q:
        i = q.popleft()
        for node, cost in road[i]:
            if dist[node] > dist[i] + cost:
                dist[node] = dist[i] + cost
                q.append((node))
    print('#{} {}'.format(t, dist[N]))