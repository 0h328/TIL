"""
2. bfs - 인접 리스트 구현
"""
# 다양한 형태의 구현 방식을 보고 써보는 것이 중요
def bfs(v):
    Q = [v]
    while Q:
        v = Q.pop(0)
        if v not in visited:              # 방문 리스트 안에 없으면
            visited.append(v)             # 방문 처리
            for w in G[v]:                # v의 인접 정점 돌며
                if w not in visited:      # 해당 정점이 아직 방문하지 않은 곳이라면
                    Q.append(w)           # Q에 넣자
    return ' -> '.join(map(str, visited))

import sys
sys.stdin = open('input.txt')
V, E = map(int, input().split())        # 정점 & 간선
temp = list(map(int, input().split()))  # 정점 정보
G = [[] for _ in range(V+1)]            # 그래프 초기화
for i in range(len(temp)//2):           # 그래프 생성
    # 0, 2, 4, 6 ...        1, 3, 5, 7 ...
    G[temp[i*2]].append(temp[i*2+1])
visited = []                            # (이전과는 다른 방식의) 방문 체크
print(bfs(1))