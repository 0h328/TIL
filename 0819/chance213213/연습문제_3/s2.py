def dfs(v):
    if not visited[v]:
        visited[v] = 1
    for w in range(V+1):
        if G[v][w] == 1 and not visited[w]:
            dfs(w) #재귀 호출, 즉 v랑 연결되어 있고, 방문 안한 정점이 있으면 그 정점을 재귀 호출한다.

import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[0] * (V+1) for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

for i in range(E):
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1
dfs(1)