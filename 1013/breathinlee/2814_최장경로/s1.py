import sys
sys.stdin = open('input.txt')

def dfs(node, cnt):
    global max_cnt

    if max_cnt < cnt:
        max_cnt = cnt

    for w in G[node]:
        if not visited[w]:
            visited[w] = 1
            dfs(w, cnt+1)
            visited[w] = 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())   # N개의 정점, M개의 간선
    G = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    max_cnt = 0
    for _ in range(M):
        x, y = map(int, input().split())
        G[x].append(y)
        G[y].append(x)

    for i in range(1, N+1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0

    print('#{} {}'.format(tc, max_cnt))