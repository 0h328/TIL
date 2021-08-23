"""
2. dfs - 인접 행렬 - 재귀
"""

def dfs(v):
    if not visited[v]:
        visited[v] = True
        print(v, visited[v], '--')

    # for node in G_list[v]:
    #     if not visited[node]:
    #         dfs(node)

    for w in range(1, V + 1):
        if G[v][w] == 1 and not visited[w]:
            dfs(w)                              # return으로 해서 종료되면 안 됨

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