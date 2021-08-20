# def dfs(v): # stack
#     stack = [v] # 시작 정점을 stack에 넣어두고 가자!
#
#     while stack:    # 모든 정점을 방문할 때까지 반복!
#         v = stack.pop()
#
#         if not visited[v]:  # 아직 방문하지 않은 정점이라면
#             visited[v] = 1  # 방문 체크!
#             print('방문 정점: {}, 방문 체크 : {}'.format(v, visited))
#
#             for w in range(1, V+1):
#                 if G[v][w] == 1 and not visited[w]: # v의 인접 정점(w)이고 그것이 아직 방문하지 않은 곳이라면
#                     stack.append(w)


from pandas import DataFrame
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    P1 = [list(map(int, input().split())) for _ in range(E)] # temp
    S, G = map(int, input().split())

    P2 = [[] for _ in range(V+1)]

    for i in range(1, len(P1), 2):
        P2[P1[i-1]].append(P1[i])
        P2[P1[i]].append(P1[i-1])

# 인접 딕셔너리


# 방문 표시 초기화
visited = [0 for _ in range(V+1)]
# print(visited)

# dfs 탐색 시작
dfs(1)    # 1번 정점부터 탐색 시작

