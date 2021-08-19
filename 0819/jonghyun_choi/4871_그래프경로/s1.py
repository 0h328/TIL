import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(v):
    stack = [v]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            for w in range(1, V+1):
                if Graph[v][w] == 1 and not visited[w]:
                    stack.append(w)






for case in range(T):
    V, E = map(int, input().split())
    Graph = [[0]* (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        x, y = map(int,input().split())
        Graph[x][y] = 1
    S, G = map(int,input().split())
    visited = [0] * (V + 1)
    dfs(S)
    if visited[G] == 0:
        print('#{} {}'.format(case + 1, 0))
    else:
        print('#{} {}'.format(case + 1, 1))
