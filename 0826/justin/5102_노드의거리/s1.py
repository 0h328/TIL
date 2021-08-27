def bfs(v):
    Q = []
    Q.append(v)         # 출발 노드를 Q에 넣고 바로 방문 처리
    visited[v] = 1
    while Q:
        v = Q.pop(0)                                # Q의 가장 앞에 있는 노드를 꺼내고
        if v == goal:                               # 만약 해당 노드가 목적지라면
            return visited[v] - 1                   # 간선은 노드 - 1
        for w in range(1, V+1):                     # 모든 정점을 반복하며
            if G[v][w] == 1 and not visited[w]:     # 인접 & 방문하지 않는 노드 찾아
                Q.append(w)                         # Q에 넣고
                visited[w] = visited[v] + 1         # 방문체크 -> 해당 노드(w)의 거리 누적
    return 0

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())                    # V(정점), E(간선)
    G = [[0 for _ in range(V+1)] for _ in range(V+1)]   # 그래프 초기화
    visited = [0 for i in range(V + 1)]                 # 방문처리
    for _ in range(E):
        sn, en = map(int, input().split())              # 그래프 초기화를 위한 연결 노드 정보
        G[sn][en] = 1                                   # 무방향 그래프
        G[en][sn] = 1
    start, goal = map(int, input().split())             # 출발노드, 도착노드
    ans = bfs(start)
    print('#{} {}'.format(tc, ans))
