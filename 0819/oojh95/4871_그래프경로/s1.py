import sys
sys.stdin = open('input.txt')
def dfs(v):
    if not visited[v]:
        visited[v] = 1
    for w in range(1, V+1):
        if Graph[v][w] == 1 and not visited[w]:
            dfs(w)


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())

    temp = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    # Graph 초기화
    Graph = [[0 for _ in range(V + 1)] for _ in range(V + 1)]

    for i in range(E):
        Graph[temp[i][0]][temp[i][1]] = 1


    visited = [0 for _ in range(V + 1)]
    dfs(S)

    if visited[G] == 0:
        print('#{} 0'.format(test_case))
    else:
        print('#{} 1'.format(test_case))