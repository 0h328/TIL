"""
1. dfs - 인접 행렬 - 반복
"""
from pandas import DataFrame

def dfs(v):
    stk = [v]

    while stk:
        p = stk.pop()
        if not visited[p]:
            visited[p] = True
            print(p, visited[p], '--')

        for node in G_list[p]:
            if not visited[node]:
                stk.append(node)
    return p


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
temp = list(map(int, input().split()))

# Graph 초기화 (인접행렬)
G = [[0] * (V + 1) for _ in range(V + 1)]
for i in range(0, V*2, 2):
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

# print(DataFrame(G))
# Graph 초기화 (인접 리스트)

G_list = [[] for _ in range(V + 1)]
for i in range(0, V*2, 2):
    G_list[temp[i]].append(temp[i+1])
    G_list[temp[i+1]].append(temp[i])

# print(G_list)

# 방문 표시 초기화
visited = [False for _ in range(V + 1)]

# dfs 탐색 시작
print(dfs(1))