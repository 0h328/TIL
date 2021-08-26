def bfs(v):
    Q = []
    Q.append(v)
    visited[v] = 1
    print('방문 정점: {}, 방문 체크: {}'.format(v, visited))

    while Q:
        v = Q.pop(0)
        for w in range(1, V+1):
            if G[w][v] and not visited[w]:
                Q.append(w)
                visited[w] = 1
                print('방문 정점: {}, 방문 체크: {}'.format(w, visited))

import sys
sys.stdin = open('input.txt')
# V(ertex), E(dge)
V, E = map(int, input().split())
# 간선 정보 초기화
temp = list(map(int, input().split()))
# Graph 초기화
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
for i in range(E):
    n1, n2 = temp[2*i], temp[2*i+1]
    G[n1][n2] = 1
    G[n2][n1] = 1
# 방문 표시 초기화
visited = [0] * (V+1)
# bfs 탐색 시작
bfs(1)