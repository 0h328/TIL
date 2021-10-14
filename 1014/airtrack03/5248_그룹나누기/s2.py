import sys

sys.stdin = open('input.txt')

T = int(input())

def dfs(start):
    global ans

    stack = [start]
    visited[start] = 1

    while stack:
        cur = stack.pop()

        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = 1
                stack.append(nxt)

    ans += 1



for tc in range(1, T+1):
    N, M = map(int, input().split())

    visited = [0] * (N+1)
    graph = [[] for _ in range(N+1)]


    data = list(map(int, input().split()))
    for i in range(M):
        v1, v2 = data[i*2], data[i*2 + 1]
        graph[v1].append(v2)
        graph[v2].append(v1)

    ans = 0
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)

    print('#{} {}'.format(tc, ans))