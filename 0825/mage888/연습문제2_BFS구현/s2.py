"""
2. bfs - 인접 리스트 구현
"""

def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        t = q.pop(0)
        print(t)
        for i in G[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[t] + 1 # 시작점부터 해당 인덱스 지점까지의 거리?

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
print(G)

# 방문 표시 초기화
visited = [0] * (V+1)

# bfs 탐색 시작
bfs(1)