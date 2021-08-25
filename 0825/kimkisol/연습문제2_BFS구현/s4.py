"""
4. bfs - 1번 노드에서 가장 멀리 떨어진 노드 찾기 (거리에 대한 정보 담아 놓기)
"""


def bfs(v):
    global visited
    Q = []
    Q.append(v)
    visited[v] = 1
    print(v, end=' ')

    while Q:
        t = Q.pop(0)
        for i in G[t]:
            if not visited[i]:
                visited[i] = visited[t] + 1
                Q.append(i)
                print(i, end=' ')
    print()
    for i in range(V + 1):
        if visited[i] == max(visited):
            print('노드번호:', i, ', 거리:', visited[i])

import sys

sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
edges = list(map(int, input().split()))

# Graph 초기화
G = [[] * (V + 1) for _ in range(V + 1)]
for i in range(E):
    G[edges[2 * i]].append(edges[2 * i + 1]) # 빈 리스트에 삽입
print(G)

# 방문 표시 초기화
visited = [0] * (V + 1)

# bfs 탐색 시작
bfs(1)
