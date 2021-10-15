def dfs(v):
    visited[v] = 1                              # 방문 체크
    for w in G[v]:
        if not visited[w]:                      # 인접 정점 중 방문하지 않은 정점 다시 방문
            dfs(w)

import sys
sys.stdin = open('input.txt')
T = int(input())
ans = []
for tc in range(1, T+1):
    N, M = map(int, input().split())            # N: 정점 / M: 간선
    G = [[] for _ in range(N+1)]

    for _ in range(M):                          # 인접 리스트 준비
        u, v = map(int, input().split())
        G[u].append(v); G[v].append(u)

    visited = [0] * (N+1)
    cnt = 0
    for i in range(1, N+1):                     # 1번부터 N번까지 반복을 돌며
        if not visited[i]:                      # 방문하지 않았다면
            cnt += 1
            dfs(i)                              # 방문
    ans.append('#{} {}'.format(tc, cnt))
print('\n'.join(ans))