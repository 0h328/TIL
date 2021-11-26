"""
2. bfs - 인접 리스트 구현
"""

def bfs(v):
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        t = queue.pop(0)
        for i in graph[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                print(i)  # 어떤 순서로 탐색했는지

import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
temp = list(map(int, input().split()))

# Graph 초기화
graph = [[] for _ in range(V+1)]
for i in range(1, len(temp), 2):
    graph[temp[i-1]].append(temp[i])
    graph[temp[i]].append(temp[i-1])
# print(graph)

# 방문 표시 초기화
visited = [0] * (V+1)

# bfs 탐색 시작
bfs(1)