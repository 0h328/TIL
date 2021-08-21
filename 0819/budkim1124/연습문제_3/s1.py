"""
1. dfs - 인접 행렬 - 반복
"""

def dfs(v):
    stack = [v] # 시작 정점을 stack에 넣어두고 가자!

    while stack:    # 모든 정점을 방문할 때까지 반복
        v = stack.pop()

        if visited[v] == 0: # 아직 방문하지 않은 정점이라면
            visited[v] = 1 # 방문 체크
            print("방문 정점 : {} , 방문 체크 : {}".format(v, visited))
        
            for w in range(1, V+1): # 모든 정점에 대한 반복을 수행하며
                if G[v][w] ==1 and not visited[w]:  # v의 인접 정점(w)이고 그곳이 아직 방문하지 않았다면
                    stack.append(w)

import sys
sys.stdin = open('input.txt')
# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
temp = list(map(int, input().split()))

# Graph 초기화
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
# print(DataFrame(G))
# 인접 행렬
for i in range(E):
    G[temp[i * 2]][temp[i * 2 + 1]] = 1
    G[temp[i * 2 + 1]][temp[i * 2]] = 1

# print("==========================")
# print(DataFrame(G))

# ## 인접 리스트
# G = [[] for _ in range(V+1)]
# for i in range(1, len(temp), 2):
#     G[temp[i - 1]].append(temp[i])
#     G[temp[i]].append(temp[i - 1])
# print(G)


# 방문 표시 초기화
visited = [0 for i in range(V+1)]
# print(visited)


# dfs 탐색 시작
dfs(1) # 1번 정점부터 탐색을 시작하겠다.
#  보통 1번 정점에서 탐색하는 것을 예로 하기 때문

