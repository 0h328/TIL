"""
1. bfs - 인접 행렬 구현
"""

def bfs(v):
    visited[v] = 1
    queue = [v]

    while queue:
        p = queue.pop(0)

        for j in range(V + 1):
            if G[p][j] and not visited[j]:
                queue.append(j)
                visited[j] = visited[p] + 1


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
tmp = list(map(int, input().split()))

# Graph 초기화
G = [[0] * (V + 1) for _ in range(V + 1)]
for i in range(E):
    s, e = tmp[i*2], tmp[i*2 + 1]
    G[s][e] = 1

# 방문 표시 초기화
visited = [0] * (V + 1)

# bfs 탐색 시작
bfs(1)
print(visited)