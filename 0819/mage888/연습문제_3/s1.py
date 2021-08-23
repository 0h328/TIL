import sys
sys.stdin = open('input.txt')
from pandas import DataFrame

def dfs(v):
    stack = [v]                # 시작 정점 stack에 넣어놓고 시작

    while stack:               # stack이 빌때까지 while len(stack) 등도 가능
        v = stack.pop()        # stack의 가장 위에서 정점을 꺼내
        print(v)

        if not visited[v]:     # 아직 방문하지 않았다면
            visited[v] = 1     # 방문 체크
            print('방문 정점: {}, 방문 체크: {}'.format(v, visited))

            for w in range(1, V+1):                     # 모든 정점에 대한 반복을 수행하며
                if G[v][w] == 1 and not visited[w]:     # 해당의 인접 정점이고 아직 방문하지 않았다면
                    stack.append(w)                     # stack에 push




# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
temp = list(map(int, input().split()))
# print(temp)

# Graph 초기화 (정점보다
G = [[0 for _ in range(V+1)] for _ in range(V+1)]

# 인접 행렬
for i in range(E):
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1
#
# print('----------------------------')
#
# print(DataFrame(G))

# 인접 리스트
# G = [[] for _ in range(V+1)]
# print(G)
#
# for i in range(1, len(temp), 2):
#     G[temp[i-1]].append(temp[i])
#     G[temp[i]].append(temp[i-1])
#
# print(G)

# 방문 표시 초기화
visited = [0 for _ in range(V+1)]
# print(visited)

# dfs 탐색 시작
dfs(1) # 1번 정점부터 탐색 시작