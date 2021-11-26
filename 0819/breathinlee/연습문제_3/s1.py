"""
1. dfs - 인접 행렬 - 반복
"""

def dfs(v):
    stack = [v] # 시작 정점을 stack에 넣어두고 가자

    while stack:  # 모든 정점을 방문할 때까지 반복
        v = stack.pop()

        if not visited[v]:  # 아직 방문하지 않은 정점이라면
            visited[v] = 1  # 방문 체크
            print('방문정점: {}, 방문체크: {}'.format(v, visited))

            for w in range(1, w+1):
                if G[v][w] == 1 and not visited[w]:  # v의 인접 정점(w)이고, 아직 방문하지 않은 곳이라면
                    stack.append(w)

from pandas import DataFrame
import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
temp = list(map(int, input().split()))

# Graph 초기화
G = [[0 for _ in range(V+1)] for _ in range(V+1)]

# 인접행렬
for i in range(E):
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1
# print(DataFrame(G))

# 인접리스트
# G = [[] for _ in range(V+1)]
#
# for i in range(1, len(temp), 2):
#     G[temp[i-1]].append(temp[i])
#     G[temp[i]].append(temp[i-1])

# 방문 표시 초기화
visited = [0 for _ in range(V+1)]  # False로 해도 됨

# dfs 탐색 시작
dfs(1)  # 1번 정점부터 탐색 시작