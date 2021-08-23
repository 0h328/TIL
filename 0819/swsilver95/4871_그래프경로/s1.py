import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(S, G):
    global V
    stk = [S]
    visited = [False for _ in range(V + 1)]

    while stk:
        p = stk.pop()
        visited[p] = True
        if visited[G]:
            return 1

        for j in range(1, V + 1):
            if graph[p][j] and not visited[j]:
                stk.append(j)

    return 0

for tc in range(1, T + 1):
    V, E = map(int, input().split())                                # V개의 노드, E개의 경로
    graph = [[False for _ in range(V + 1)] for _ in range(V + 1)]
    for _ in range(E):
        n, m = map(int, input().split())
        graph[n][m] = True

    S, G = map(int, input().split())

    print('#{} {}'.format(tc, dfs(S, G)))