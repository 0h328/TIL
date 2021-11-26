# 인접 리스트 - 재귀

def dfs(v):
    visited[v] = 1                                          # 방문 체크
    print('방문 정점: {}, 방문 체크: {}'.format(v, visited))
    for w in G[v]:                                          # 정점 v의 인접 정점 w 중에서
        if not visited[w]:                                  # 아직 방문하지 않은 곳이 있다면
            dfs(w)                                          # 호출!
n
import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]
# [[], [], []]
for i in range(1, len(temp), 2):
    G[temp[i-1]].append(temp[i])
    G[temp[i]].append(temp[i-1])

dfs(1)