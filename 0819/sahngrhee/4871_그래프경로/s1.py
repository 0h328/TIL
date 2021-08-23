# def dfs(v):
#     stack = [v]
#     while stack:
#         v = stack.pop()
#         if not visited[v]:
#             visited[v] = 1
#             print('방문 정점: {}, 방문 체크: {}'.format(v, visited))
#             for w in range(1, V+1):
#                 if Graph[v][w] == 1 and not visited[w]:
#                     stack.append(w)

from pandas import DataFrame
import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    temp = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    Graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    for i in range(E):
        Graph[temp[i][0]][temp[i][1]] = 1

    stack = [S]
    ans = 0

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            # print('방문 정점: {}, 방문 체크: {}'.format(v, visited))
            for w in range(1, V + 1):
                if Graph[v][w] == 1 and not visited[w]:
                    stack.append(w)

    if visited[G] == 1:
        ans = 1
    print('#{} {}'.format(test_case, ans))
