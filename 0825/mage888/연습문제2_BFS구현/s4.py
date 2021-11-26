"""
4. bfs - 1번 노드에서 가장 멀리 떨어진 노드 찾기 (거리에 대한 정보 담아 놓기)
"""

def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        t = q.pop(0)
        for i in G[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[t] + 1

    node = 0
    distance = 0
    for idx, val in enumerate(visited):
        if distance < val:
            node, distance = idx, val
    print(node)

import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
edge = list(map(int, input().split()))

# Graph 초기화
G = [[] for _ in range(V+1)]

for i in range(E):
    n1, n2 = edge[2*i], edge[2*i+1]
    G[n1].append(n2)
    G[n2].append(n1)

# 방문 표시 초기화
visited = [0] * (V+1)

# bfs 탐색 시작
bfs(1)