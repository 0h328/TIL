"""
1. bfs - 인접 행렬 구현
"""
import sys
sys.stdin = open('input.txt')

def bfs(v):
    queue = [v]
    visited[v] = 1

    while queue:
        cur = queue.pop(0)
        print('방문 정점: {}, 방문 체크: {}'.format(cur, visited))
        for w in range(1, V+1):
            if G[cur][w] == 1 and not visited[w]:
                queue.append(w)
                visited[w] = 1

# V(ertex), E(dge)
V, E = map(int, input().split())
# 간선 정보 초기화
temp = list(map(int, input().split()))
# Graph 초기화
G = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    G[temp[2*i]][temp[2*i+1]] = 1
    G[temp[2*i+1]][temp[2*i]] = 1
# 방문 표시 초기화
visited = [0 for _ in range(V+1)]
# bfs 탐색 시작
bfs(1)