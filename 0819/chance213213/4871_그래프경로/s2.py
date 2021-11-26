import sys
sys.stdin = open('input.txt')

def dfs(v, goal):
    if not visited[v]:
        visited[v] = 1
    for w in range(V+1):
        if G[v][w] == 1 and not visited[w]:
            dfs(w, goal)
    return visited[goal]

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    temp = [list(map(int, input().split())) for _ in range(E)]
    G = [[0] * (V+1) for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    st, en = map(int, input().split())
    for i in range(E):
        G[temp[i][0]][temp[i][1]] = 1
        G[temp[i][1]][temp[i][0]] = 1
    ans = dfs(st, en)
    print('#{} {}'.format(tc, ans))

