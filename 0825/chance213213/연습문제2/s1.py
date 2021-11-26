"""
1. bfs - 인접 행렬 구현
"""

def bfs(v):
    Q = [v]
    while Q:
        v = Q.pop(0)
        if not visited[v]:
            visited[v] = 1
            for w in range(1, V+1):
                if G[v][w] == 1 and not visited[w]:
                    Q.append(w)

import sys
sys.stdin = open('input.txt')
V, E = map(int, input().split())
temp = list(map(int, input().split()))

G = [[0 for _ in range(V+1)] for _ in range(V+1)]
for i in range(len(temp)//2):
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1

visited = [0] * (V+1)

# V(ertex), E(dge)

# 간선 정보 초기화

# Graph 초기화

# 방문 표시 초기화

# bfs 탐색 시작
bfs(1)