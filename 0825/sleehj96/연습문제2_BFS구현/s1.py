"""
1. bfs - 인접 행렬 구현
"""

def bfs(v):
    q = list()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        for w in range(V+1):
            if G[v][w] == 1 and not visited[w]:
                q.append(w)
                visited[w] = 1


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
edges = list(map(int, input().split()))

# Graph 초기화
G = [[0 for _ in range(V+1)] for _ in range(V+1)]

for i in range(E):
    G[edges[i*2]][edges[i*2+1]] = 1
    G[edges[i*2+1]][edges[i*2]] = 1

# 방문 표시 초기화
visited = [0 for _ in range(V+1)]

# bfs 탐색 시작
print(visited)
bfs(1)
print(visited)