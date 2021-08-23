"""
3. dfs - 인접 리스트
"""

def dfs(v):
    stack = [v]  # 시작 정점을 stack에 넣기

    while stack:  # 모든 정점을 방문할 때까지 반복
        v = stack.pop()

        if not visited[v]:  # 아직 방문하지 않은 정점이라면
            visited[v] = 1
            print('방문 정점: {}, 방문 체크: {}'.format(v, visited))

            for w in range(len(graph[v])):
                if not visited[graph[v][w]]:  # v의 인접정점이고 아직 방문하지 않은 곳이라면
                    stack.append(graph[v][w])


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
temp = list(map(int, input().split()))

# Graph 초기화 (인접리스트)
graph = [[] for _ in range(V+1)]
for i in range(1, len(temp), 2):
    graph[temp[i-1]].append(temp[i])
    graph[temp[i]].append(temp[i-1])
print(graph)

# 방문 표시 초기화
visited = [0 for _ in range(V+1)]

# dfs 탐색 시작
dfs(1)
print(visited)