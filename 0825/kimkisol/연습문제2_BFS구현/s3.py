"""
3. bfs - 인접 딕셔너리 구현
"""


def bfs(v):
    global visited
    Q = []
    Q.append(v)
    visited[v] = 1
    print(v, end=' ')

    while Q:
        t = Q.pop(0)
        for i in G.get(t, []):
            if not visited[i]:
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
G = {}
for i in range(E):
    G[edges[2 * i]] = G.get(edges[2 * i], []) + [edges[2 * i + 1]] # 키 값이 없을 때 value를 추가할 리스트 생성 방법
print(G)

# 방문 표시 초기화
visited = [0] * (V + 1)

# bfs 탐색 시작
bfs(1)
