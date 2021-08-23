"""
1. dfs - 인접 행렬 - 반복
"""

def dfs(v):
    stack = [v]

    while stack:
        v = stack.pop()

        if not visited[v]:
            visited[v] = 1

            for w in range(1, V+1):
                if graph[v][w] == 1 and not visited[w]: # 인접 정점이고, 그곳에 방문하지 않았다면
                    stack.append(w)

# recursion
def dfs_2(v):
    if not visited[v]:
        visited[v]
    for w in range(1, V+1):
        if graph[v][w] == 1 and not visited[w]:
            dfs(w)

import sys
import pandas as pd

sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
tmp = list(map(int, input().split()))

# Graph 초기화
graph = [[0 for _ in range(V+1)] for _ in range(V+1)]

for i in range(E):
    graph[tmp[i*2]][tmp[i*2+1]] = graph[tmp[i*2+1]][tmp[i*2]] = 1
# df = pd.DataFrame(graph, index=list(range(10, 18)), columns=list(range(10, 18)))
# print(df)


# 방문 표시 초기화
visited = [False for _ in range(V+1)]

# dfs 탐색 시작
dfs(1)