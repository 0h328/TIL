def dfs(v):
    visited[v] = 1
    for w in G[v]:
        if not visited[w]:
            dfs(w)

import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[] for _ in range(V+1)] # 각 정점마다 연결되어 있는 정점을 적어주는 리스트 생성
visited = [0 for _ in range(V+1)]

for i in range(1, len(temp), 2):
    G[temp[i-1]].append(temp[i])
    G[temp[i]].append(temp[i-1])
print(G)
