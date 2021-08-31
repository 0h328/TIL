import sys
sys.stdin = open('input.txt')

from collections import deque

for T in range(int(input())):
    V, E = map(int, input().split())
    graph = {i:[] for i in range(V+1)}
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    S, G = map(int, input().split())
    visitied = [0]*(V+1)

    q = deque([S])
    while q:
        v = q.popleft()
        for next_v in graph[v]:
            if not visitied[next_v]:
                visitied[next_v]=visitied[v]+1
                q.append(next_v)

    ans = visitied[G]
    print('#{} {}'.format((T+1), ans))

#1 2
#2 4
#3 3
