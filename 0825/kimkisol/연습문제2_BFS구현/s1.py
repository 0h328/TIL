"""
1. bfs - 인접 행렬 구현
"""


def bfs(v):
    global visited
    Q = []
    Q.append(v)
    visited[v] = 1
    print(v, end=' ')

    while Q:
        t = Q.pop(0)
        for i in range(1, len(G[t])):
            if G[t][i] == 1 and not visited[i]:
                visited[i] = 1
                Q.append(i)
                print(i, end=' ')


import sys

sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
edges = list(map(int, input().split()))

# Graph 초기화
G = [[0] * (V + 1) for _ in range(V + 1)]
for i in range(E):
    G[edges[2 * i]][edges[2 * i + 1]] = 1
    G[edges[2 * i + 1]][edges[2 * i]] = 1 # 방향이 없기 때문에 반대쪽도 꼭 해줘야 됨
print(G)

# 방문 표시 초기화
visited = [0] * (V + 1)

# bfs 탐색 시작
bfs(1)
