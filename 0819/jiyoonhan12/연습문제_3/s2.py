"""
2. dfs - 인접 행렬 - 재귀
"""

def dfs(v):
    if not visited[v]:
        visited[v] = 1

    for w in range(1, V+1):
        if graph[v][w] == 1 and not visited[w]:
            dfs(w)


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
temp = list(map(int, input().split()))
# print(temp)

# Graph 초기화 (인접행렬)
graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
for i in range(E):
    graph[temp[i*2]][temp[i*2+1]] = 1
    graph[temp[i*2+1]][temp[i*2]] = 1

# 방문 표시 초기화
visited = [0 for _ in range(V+1)]
print(visited)

# dfs 탐색 시작
dfs(1)