def bfs(sv):
    Q = [[sv, 0]]           # 정점 & 거리 정보를 같이 기록
    visited[sv] = 1         # 방문처리
    while Q:
        v, distance = Q.pop(0)
        if v == ev:
            return distance
        for w in range(1, V+1):
            if G[v][w] and not visited[w]:
                Q.append([w, distance+1])
                visited[w] = 1
    return 0

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        a, b = map(int, input().split())
        G[a][b] = G[b][a] = 1
    sv, ev = map(int, input().split())
    ans = bfs(sv)
    print('#{} {}'.format(tc, ans))

