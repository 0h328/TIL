"""
1. dfs - 인접 행렬 - 반복
"""
import sys
sys.stdin = open('input.txt')


def dfs(v):
    stack = [v]

    while stack:
        v = stack.pop()

        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')

            for w in range(1, V+1):
                if G[v][w] == 1 and not visited[w]:
                    stack.append(w)


# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
temp = list(map(int, input().split()))

# Graph 초기화
G = [[0 for _ in range(V+1)] for _ in range(V+1)]

for i in range(E):
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1

# 방문 표시 초기화
visited = [0 for _ in range(V+1)]

# dfs 탐색 시작
dfs(1)
