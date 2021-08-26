def bfs(s, V):
    q = []                          # 큐 생성
    visited = [0]*(V+1)             # visited 생성
    q.append(s)                     # 시작점 인큐
    visited[s] = 1                  # 시작점 visited 표시
    while q:                        # 큐가 비어있지 않으면 (처리할 정점이 남아 있으면)
            t = q.pop(0)            # 디큐(꺼내서)해서 t에 저장
            if t == G:
                return visited[t] - 1
            for i in range(1, V+1): # t에 인접이고 미방문인 모든 i에 대해
                if adj[t][i] == 1 and visited[i] == 0:
                    q.append(i)                     # enqueue(i)
                    visited[i] = visited[t] + 1     # i visited로 표시

    return 0

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]  # 인접행렬

    for i in range(E):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1
        adj[n2][n1] = 1

    S, G = map(int, input().split())

    print('#{} {}'.format(tc, bfs(S, V)))
