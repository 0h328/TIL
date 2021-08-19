"""
1. dfs - 인접 행렬 - 반복
"""

def dfs(v):
    visited[v] = 1
    stack = []
    k = v
    while True:
        for w in range(1, V+1):
            if G[k][w] == 1 and visited[w] == 0:
                stack.append(k)
                k = w
                visited[w] = 1
                break
        else:
            if stack:
                k = stack.pop()
            else:
                break





import sys
from pandas import DataFrame

sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화 (정점 연결 정보)
temp = list(map(int, input().split()))
# print(temp)

# Graph 초기화
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
for i in range(0, len(temp), 2):
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1
# print(DataFrame(G))

# 방문 표시 초기화
visited = [0] * (V+1)

# dfs 탐색 시작
dfs(1)
print(visited)
