"""
1. dfs - 인접 행렬 - 반복
"""

def dfs(v):
    stack = [v]

    while stack:
        v = stack.pop()

        if not visited[v]:
            visited[v] = 1
            print('방문 정점: {}, 방문 체크: {}'.format(v, visited))

            for w in range(1, V+1):
                if G[v][w] == 1 and not visited[w]:   # 아직 w가 방문한 정점이 아니라면
                    stack.append(w)



import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int,input().split())

# 간선 정보 초기화
temp = list(map(int,input().split()))
print(temp)

# Graph 초기화
G = [[0 for _ in range(V+1)]for _ in range(V+1)]
print(G)

# 인접 행렬
for i in range(E):
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1

print(G)

# 인접 리스트

# G = [[] for _ in range(V+1)]
#
# for i in range(1, len(temp), 2):
#     G[temp[i-1]].append(temp[i])
#     G[temp[i]].append(temp[i-1])
# print(G)


# 방문 표시 초기화
visited = [0 for _ in range(V+1)]
print(visited)

# dfs 탐색 시작
dfs(1)