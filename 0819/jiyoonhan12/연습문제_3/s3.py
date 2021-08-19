"""
3. dfs - 인접 리스트
"""

def dfs(v):
    pass


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
temp = list(map(int, input().split()))

# Graph 초기화 (인접리스트)
graph = [[] for _ in range(V+1)]
for i in range(1, len(temp), 2):
    graph[temp[i-1]].append(temp[i])
    graph[temp[i]].append(temp[i-1])
#print(graph)

# 방문 표시 초기화
visited = [0 for _ in range(V+1)]
print(visited)
dfs(1)

# dfs 탐색 시작
dfs(1)