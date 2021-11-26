"""
3. bfs - 인접 딕셔너리 구현
"""
# 다양한 형태의 구현 방식을 보고 써보는 것이 중요
def bfs(v):
    not_visited.append(v)               # 방문하지 않은 리스트에 추가
    while not_visited:                  # 모든 정점을 다 탐색할 때까지 진행
        v = not_visited.pop(0)          # 리스트의 가장 앞에 있는 정점을 뽑아
        if v not in visited:            # 해당 정점이 방문하지 않은 곳이라면
            visited.append(v)           # 방문 체크
            not_visited.extend(G[v])    # 해당 정점과 연결된 인접 정점을 방문하지 않은 리스트에 연결
    return ' -> '.join(map(str, visited))

import sys
sys.stdin = open('input.txt')
V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = {}                          # 연결 정점 정보 그래프 생성(무방향 그래프) -> 각 정점에 필요한 정보를 넣기 위한 준비
for i in range(1, V+1):
    G[i] = []

# print(G)
for i in range(0, len(temp), 2):
    G[temp[i]].append(temp[i+1])
    G[temp[i+1]].append(temp[i])

# print(G)
# 다른 방식의 방문체크
visited = []
not_visited = []
print(bfs(1))