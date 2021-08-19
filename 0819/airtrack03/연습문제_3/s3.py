"""
3. dfs - 인접 리스트
"""

def dfs(v):
    visited[v] = 1
    print('방문 정점: {}, 방문 체크: {}'.format(v, visited))
    for w in G[v]:
        if not visited[w]:
            dfs(w)


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
temp = list(map(int, input().split()))

# 인접 리스트
G = [[] for _ in range(V+1)]
for i in range(1, len(temp), 2):
    G[temp[i-1]].append(temp[i])
    G[temp[i]].append(temp[i-1])

# 방문 표시 초기화
visited = [0 for _ in range(V+1)]

# dfs 탐색 시작
dfs(1)