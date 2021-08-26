"""
2. bfs - 인접 리스트 구현
"""


def bfs(v):
    visited[v] = 1
    queue = [v]

    while queue:
        p = queue.pop(0)

        for node in G[p]:
            if not visited[node]:
                queue.append(node)
                visited[node] = visited[p] + 1


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
tmp = list(map(int, input().split()))

# Graph 초기화
G = [[] for _ in range(V + 1)]
for i in range(E):
    s, e = tmp[i*2], tmp[i*2 + 1]
    G[s].append(e)

# 방문 표시 초기화
visited = [0] * (V + 1)

# bfs 탐색 시작
bfs(1)
print(visited)