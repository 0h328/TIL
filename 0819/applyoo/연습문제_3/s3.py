"""
3. dfs - 인접 리스트
"""
import sys
sys.stdin = open('input.txt')


def dfs(v):
    if not visited[v]:
        visited[v] = 1
        print(v, end=' ')

    for w in G[v]:
        if not visited[w]:
            dfs(w)


# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
temp = list(map(int, input().split()))

# Graph 초기화
G = [[] for _ in range(V+1)]

for i in range(1, len(temp), 2):
    G[temp[i-1]].append(temp[i])
    G[temp[i]].append(temp[i-1])

# 방문 표시 초기화
visited = [0 for _ in range(V+1)]

# dfs 탐색 시작
dfs(1)
