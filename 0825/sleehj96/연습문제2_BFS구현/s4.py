"""
4. bfs - 1번 노드에서 가장 멀리 떨어진 노드 찾기 (거리에 대한 정보 담아 놓기)
"""

def bfs(v):
    q = list()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        for w in G[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v]+1


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
edges = list(map(int, input().split()))

# Graph 초기화
G = [[] for _ in range(V+1)]
for i in range(E):
    G[edges[2*i]].append(edges[2*i+1])
    G[edges[2 * i+1]].append(edges[2 * i])

# 방문 표시 초기화
visited = [0 for _ in range(V+1)]

# bfs 탐색 시작
# print(visited)
bfs(1)
# print(visited)
for i in range(V, 0, -1):
    if i in visited:
        print(visited.index(i))
        break