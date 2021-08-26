import sys
from pandas import DataFrame
sys.stdin = open('input.txt')


def bfs(v):
    q = list()
    visited[v] = 1
    q.append(v)

    while q:
        v = q.pop(0)

        if visited[G]:
            return

        for w in edges[v]:
            if not visited[w]:
                visited[w] = visited[v] + 1
                q.append(w)


T = int(input())
tc = 1
while tc <= T:
    V, E = map(int, input().split())

    edges = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        edges[s].append(e)
        edges[e].append(s)
    # print(edges)

    visited = [0 for _ in range(V+1)]

    S, G = map(int, input().split())

    bfs(S)
    if visited[G]:
        ans = visited[G] - 1
    else:
        ans = 0
    print('#{0} {1}'.format(tc, ans))
    tc += 1
