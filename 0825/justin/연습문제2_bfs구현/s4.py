"""
4. bfs - 1번 노드에서 가장 멀리 떨어진 노드 찾기 (거리에 대한 정보 담아 놓기)
"""
# 다양한 형태의 구현 방식을 보고 써보는 것이 중요
def bfs(v):
    Q = [v]        # Q 생성 & 바로 정점 정보 추가
    visited[v] = 1 # 방문 처리

    while Q:
        v = Q.pop(0)
        for w in range(V+1):
            if G[v][w] == 1 and not visited[w]:
                visited[w] = visited[v] + 1
                Q.append(w)

    max_dist = max(visited)
    max_dist_vertex = visited.index(max_dist)
    return max_dist_vertex

import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
temp = list(map(int, input().split()))

# Graph 초기화
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
for i in range(E):
    G[temp[2*i]][temp[2*i+1]] = 1
    G[temp[2*i+1]][temp[2*i]] = 1

# 방문 표시 초기화
visited = [0 for _ in range(V+1)]

# bfs 탐색 시작
print(bfs(1))