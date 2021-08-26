"""
1. bfs - 인접 행렬 구현
"""

# 다양한 형태의 구현 방식을 보고 써보는 것이 중요
def bfs(v):
    Q = [v]                 # Q 생성 & 시작 정점 넣어놓고
    while Q:                # Q가 빌때까지
        v = Q.pop(0)        # Q에서 정점을 꺼내고
        if not visited[v]:  # 해당 정점에 방문하지 않았다면
            visited[v] = 1  # 방문체크
            print('{}번 정점에 방문'.format(v))
            for w in range(1, V+1):                  # 모든 정점 반복을 돌며
                if G[v][w] == 1 and not visited[w]:  # 해당 정점의 인접 정점이고 방문 안했다면
                    Q.append(w)                      # Q에 넣자

import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
temp = list(map(int, input().split()))

# Graph 초기화
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
for i in range(len(temp)//2):
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1

# 방문 표시 초기화
visited = [0] * (V+1)

# bfs 탐색 시작
bfs(1)