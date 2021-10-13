import sys
sys.stdin = open('input.txt')

def dfs(cur, cnt):
    global ans

    if ans < cnt:
        ans = cnt

    for nxt in graph[cur]:
        if not visited[nxt]:
            visited[nxt] = 1
            dfs(nxt, cnt+1)
            visited[nxt] = 0

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    graph = [[] for _ in range(N+1)]

    ans = 1

    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    visited = [0] * (N+1)
    for i in range(1, N+1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0

    print('#{} {}'.format(tc, ans))