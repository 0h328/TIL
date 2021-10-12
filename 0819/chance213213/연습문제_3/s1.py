def dfs(v):
    stack = [v] #시작 정점
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            for w in range(1, V+1):
                if G[v][w] == 1 and not visited[w]:
                    stack.append(w)

import sys
import pprint

sys.stdin = open('input.txt')

V, E = map(int, input().split())

graphs = list(map(int, input().split()))

G = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

for i in range(E):
    G[graphs[2*i]][graphs[2*i+1]] = 1
    G[graphs[2*i+1]][graphs[2*i]] = 1
pprint.pprint(G)
dfs(1)