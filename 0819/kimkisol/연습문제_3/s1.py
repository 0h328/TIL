import sys
sys.stdin = open('input.txt')

"""
1. dfs - 인접 행렬 - 반복
"""

def dfs(v):
    pass

import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
temp = list(map(int, input().split()))
print(temp)

# Graph 초기화
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
print(G)

#인접 행렬
for i in range(E):
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1
print(G)

#인접 리스트
G2 = [[] for _ in range(V+1)]
print(temp)
for i in range(1, len(temp), 2):
    G2[temp[i-1]].append(temp[i])
    G2[temp[i]].append(temp[i-1])
print(G2)

# 방문 표시 초기화
visited = [0 for _ in range(V+1)]

# dfs 탐색 시작
dfs(1)