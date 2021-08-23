"""
2. dfs - 인접 행렬 - 재귀
"""

def dfs(v):
    visited[v] = 1
    for w in range(V+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)


import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
temp = list(map(int, input().split()))

# Graph 초기화
G = [[0 for _ in range(V+1)] for _ in range(V+1)]

for i in range(0, len(temp), 2):
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

print(DataFrame(G))

# 방문 표시 초기화
visited = [0] * (V+1)

# dfs 탐색 시작
dfs(1)
print(visited)